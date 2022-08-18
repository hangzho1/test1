# ipex_inference.py
import argparse
import numpy as np
import pandas as pd
from time import time
import torch
from torch.utils.data import TensorDataset, DataLoader
# from torch.utils.tensorboard import SummaryWriter
from dataldr import AltranDataset
import os 
import logging
# sudo cpupower frequency-set -g performance

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', type=str, dest='input_path', help='input dataset path', default='stats_ue.csv')      
    parser.add_argument('-l', '--lookback', type=int, dest='lookback', help='lookback', default=320)
    parser.add_argument('-o', '--horizon', type=int, dest='horizon', help='horizon', default=40)
    parser.add_argument('-b', '--batch_size', type=int, dest='batch_size', help='batch_size', default=1)
    parser.add_argument('-ls', '--levels', type=int, dest='levels', help='levels', default=8)
    parser.add_argument('-hu', '--hidden_units', type=int, dest='hidden_units', help='hidden_units', default=48)
    parser.add_argument('-k', '--kernel_size', type=int, dest='kernel_size', help='kernel_size', default=3)
    parser.add_argument('-d', '--dropout', type=float, dest='dropout', help='dropout', default=0.1)       
    parser.add_argument('-lm', '--load_model_path', type=str, dest='load_model_path', help='load_model_path', default='./tcn.pth')        
    parser.add_argument('-category', '--inference_category', type=str, dest='inference_category', help='inference_category', default='pytorch_default')        
    parser.add_argument('-config', '--config_path', type=str, dest='config_path', help='config_path', default='./best_configure.json') 
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    input_path = args.input_path
    lookback = args.lookback
    horizon = args.horizon
    batch_size = args.batch_size
    levels = args.levels
    hidden_units = args.hidden_units
    kernel_size = args.kernel_size
    dropout = args.dropout
    load_model_path = args.load_model_path
    category = args.inference_category
    config_path = args.config_path

    input_size = 2
    num_channels = [hidden_units] * (levels-1) + [input_size]
    output_size = horizon

    # data
    df = pd.read_csv(input_path)
    dataset_test = AltranDataset(df, mode="test", tx=lookback, ty=horizon)
    test_loader = DataLoader(dataset_test, batch_size=batch_size, num_workers=4)
    total_test_step = len(test_loader) 
    data_shape = total_test_step*batch_size   

    if category == 'pytorch_default' or category == 'pytorch_ipex':
        from tcn_model import TemporalConvNet
        model = TemporalConvNet(past_seq_len=lookback,
                    feature_num=input_size, 
                    future_seq_len=horizon, 
                    num_channels=num_channels,
                    dropout=dropout,
                    kernel_size=kernel_size
                    )
        model.eval()
        model.load_state_dict(torch.load(load_model_path, map_location=torch.device('cpu')))
        if category == 'pytorch_ipex':
            print('Translate model to ipex model!')
            import intel_extension_for_pytorch as ipex
            model.to()
            model = ipex.optimize(model, dtype=torch.float32, level='O1')
        mse = 0
        time_test_diff = 0
        with torch.no_grad():
            for _ in range(100):
                data_warmup = torch.randn((batch_size, lookback, input_size))
                model(data_warmup)
            for data in test_loader:
                x, y_hat  = data
                if category == 'pytorch_ipex':
                    x.to()
                time_test_start = time()
                y_pred = model(x)
                time_test_end = time()
                time_test_diff = time_test_diff + (time_test_end - time_test_start)
                mse = mse + np.sum(np.square(y_hat.numpy() - y_pred.numpy()))
        latency = (time_test_diff*1000)/data_shape
        throughput = data_shape/time_test_diff
        mse = mse/(data_shape*horizon*input_size)

        print('-------- Predict Process --------')
        print('Category: {category}'.format(category=category))
        print('Data Length: {data_shape}'.format(data_shape=data_shape))
        print('FP32 IPEX Latency (ms): {latency} \nFP32 IPEX Throughput (item/s): {throughput} \nFP32 IPEX MSE: {mse}'.format(latency=latency,
                                                                                throughput=throughput,
                                                                                mse=mse))

    if category == 'pytorch_default_int8' or category == 'pytorch_ipex_int8':
        from tcn_model import TemporalConvNet as TCN_quantized
        from torch.quantization import quantize_fx
        int8_model = TCN_quantized(past_seq_len=lookback,
            feature_num=input_size, 
            future_seq_len=horizon, 
            num_channels=num_channels,
            dropout=dropout,
            kernel_size=kernel_size
            )     
        int8_model.eval()

        if category == 'pytorch_default_int8':
            qconfig_dict = {"": torch.quantization.get_default_qconfig('fbgemm')}
            int8_model = quantize_fx.prepare_fx(int8_model, qconfig_dict)
            int8_model = quantize_fx.convert_fx(int8_model)
            int8_model.load_state_dict(torch.load(load_model_path, map_location=torch.device('cpu')))

        elif category == 'pytorch_ipex_int8':
            import intel_extension_for_pytorch as ipex
            import torch.fx.experimental.optimization as optimization
            int8_model.load_state_dict(torch.load(load_model_path, map_location=torch.device('cpu'))) 
            int8_model.eval()  
            with torch.no_grad():
                ipex_config_path = config_path
                conf = ipex.quantization.QuantConf(configure_file=ipex_config_path)
                int8_model = optimization.fuse(int8_model, inplace=True)  
                x = torch.randn(batch_size, lookback, input_size)
                int8_model = ipex.quantization.convert(int8_model, conf, x)
                int8_model(x)
                

        mse = 0                                                                        
        time_test_diff = 0
        with torch.no_grad():
            for _ in range(100):
                data_warmup = torch.randn((batch_size, lookback, input_size))
                int8_model(data_warmup)            
            for data in test_loader:
                x, y_hat  = data
                time_test_start = time()
                y_pred = int8_model(x)
                # y_pred = int8_model(x)
                time_test_end = time()
                time_test_diff = time_test_diff + (time_test_end - time_test_start)
                mse = mse + np.sum(np.square(y_hat.numpy() - y_pred.numpy()))
        latency = (time_test_diff*1000)/data_shape
        throughput = data_shape/time_test_diff
        mse = mse/(data_shape*horizon*input_size)

        print('-------- Predict Process --------')
        print('Category: {category}'.format(category=category))
        print('Data Length: {data_shape}'.format(data_shape=data_shape))
        print('INT8 IPEX Latency (ms): {latency} \nINT8 IPEX Throughput (item/s): {throughput} \nINT8 IPEX MSE: {mse}'.format(latency=latency,
                                                                                throughput=throughput,
                                                                                mse=mse))


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f"\nTotal execution time: {(end - start)} seconds")  
