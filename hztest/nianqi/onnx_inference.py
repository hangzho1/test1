# onnx_inference.py
import tqdm
import numpy as np
from time import time
import pandas as pd
from dataldr import AltranDataset
from torch.utils.data import DataLoader
import onnx
import onnxruntime
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', type=str, dest='input_path', help='input dataset path', default='stats_ue.csv')     
    parser.add_argument('-l', '--lookback', type=int, dest='lookback', help='lookback', default=320)
    parser.add_argument('-o', '--horizon', type=int, dest='horizon', help='horizon', default=40)  
    parser.add_argument('-b', '--batch_size', type=int, dest='batch_size', help='batch size', default=1)       
    parser.add_argument('-lm', '--load_model_path', type=str, dest='load_model_path', help='load model path', required=True) 
    args = parser.parse_args()
    return args


def onnx_evaluate(onnx_model_path, input_path, batch_size, lookback, horizon):
    df = pd.read_csv(input_path)
    dataset_test = AltranDataset(df, mode="test", tx=lookback, ty=horizon)
    test_loader = DataLoader(dataset_test, batch_size=batch_size, num_workers=1)
    data_shape =  len(test_loader)*batch_size  
    input_size = 2

    # onnxruntime.get_all_providers()
    print('All available providersL {}'.format(onnxruntime.get_available_providers()))
    onnx_model = onnx.load(onnx_model_path)
    onnx.checker.check_model(onnx_model)
    providers = ['CPUExecutionProvider']  # 'CPUExecutionProvider', 'OpenVINOExecutionProvider'
    opts = onnxruntime.SessionOptions()
    opts.inter_op_num_threads = 1
    opts.intra_op_num_threads = 1
    ort_session = onnxruntime.InferenceSession(onnx_model_path, providers=providers, sess_options=opts)

    # compute ONNX Runtime output prediction
    mse = 0
    time_test_diff = 0
    for x, y_hat in tqdm.tqdm(test_loader):
        ort_inputs = {ort_session.get_inputs()[0].name: x.numpy()}
        start_time = time()
        y_pred = ort_session.run(None, ort_inputs)
        end_time = time()
        time_test_diff = (end_time-start_time) + time_test_diff
        mse = mse + np.sum(np.square(y_hat.numpy() - y_pred))   
    latency = (time_test_diff*1000)/data_shape
    throughput = data_shape/time_test_diff    
    mse = mse/(data_shape*horizon*input_size)    
    
    print('Num of batch size: {}'.format(len(test_loader)))   
    if  onnx_model_path.find('int8') == -1:
        print("FP32 Onnx time test MSE: {}".format(mse))
        print("FP32 Onnx time test latency (ms): {}".format(latency))
        print("FP32 Onnx time test throughput (item/s): {}".format(throughput))
    else:
        print("INT8 Onnx time test MSE: {}".format(mse))
        print("INT8 Onnx time test latency (ms): {}".format(latency))
        print("INT8 Onnx time test throughput (item/s): {}".format(throughput))

def main():
    args = parse_args()
    input_path = args.input_path
    lookback = args.lookback
    horizon = args.horizon
    load_model_path = args.load_model_path
    batch_size = args.batch_size
    onnx_evaluate(load_model_path, input_path, batch_size, lookback, horizon)    

if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f"\nTotal execution time: {(end - start)} seconds")
