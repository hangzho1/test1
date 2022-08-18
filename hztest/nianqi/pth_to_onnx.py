# pth_to_onnx.py

import argparse
from time import time
import torch
from tcn_model import TemporalConvNet

# sudo cpupower frequency-set -g performance

def parse_args():
    parser = argparse.ArgumentParser()    
    parser.add_argument('-l', '--lookback', type=int, dest='lookback', help='lookback', default=320)
    parser.add_argument('-o', '--horizon', type=int, dest='horizon', help='horizon', default=40)
    parser.add_argument('-b', '--batch_size', type=int, dest='batch_size', help='batch_size', default=1)
    parser.add_argument('-ls', '--levels', type=int, dest='levels', help='levels', default=8)
    parser.add_argument('-hu', '--hidden_units', type=int, dest='hidden_units', help='hidden_units', default=48)
    parser.add_argument('-k', '--kernel_size', type=int, dest='kernel_size', help='kernel_size', default=3)
    parser.add_argument('-d', '--dropout', type=float, dest='dropout', help='dropout', default=0.1)       
    parser.add_argument('-sm', '--save_model_path', type=str, dest='save_model_path', help='save_model_path', default='./tcn.onnx')        
    parser.add_argument('-lm', '--load_model_path', type=str, dest='load_model_path', help='load_model_path', default='./tcn.pth')         
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    lookback = args.lookback
    horizon = args.horizon
    batch_size = args.batch_size
    levels = args.levels
    hidden_units = args.hidden_units
    kernel_size = args.kernel_size
    dropout = args.dropout
    save_model_path = args.save_model_path
    load_model_path = args.load_model_path

    input_size = 2
    num_channels = [hidden_units] * (levels-1) + [input_size]

    # model
    model = TemporalConvNet(past_seq_len=lookback,
                feature_num=input_size, 
                future_seq_len=horizon, 
                num_channels=num_channels,
                dropout=dropout,
                kernel_size=kernel_size
                )    
    model.load_state_dict(torch.load(load_model_path, map_location=torch.device('cpu')))
    model.eval()

    # Export the model
    onnx_save_path = save_model_path
    x = torch.randn(batch_size, lookback, input_size)
    torch.onnx.export(model,                     # model being run
                    x,                         # model input (or a tuple for multiple inputs)
                    onnx_save_path,            # where to save the model (can be a file or file-like object)
                    export_params=True,        # store the trained parameter weights inside the model file
                    opset_version=12,          # the ONNX version to export the model to
                    do_constant_folding=True,  # whether to execute constant folding for optimization
                    input_names = ['input'],   # the model's input names
                    output_names = ['output'], # the model's output names
                    dynamic_axes={'input' : {0 : 'batch_size'},    # variable lenght axes
                                    'output' : {0 : 'batch_size'}})

    print('Save onnx model: ', onnx_save_path)


if __name__ =='__main__':
    main()
