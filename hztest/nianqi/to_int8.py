# to_int8.py
from imp import load_compiled
from nis import cat
from neural_compressor.experimental import Quantization, common
import pandas as pd
import numpy as np
import argparse
import torch
from dataldr import AltranDataset

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
    parser.add_argument('-lr', '--learning_rate', type=float, dest='learning_rate', help='learning_rate', default=0.001)  
    parser.add_argument('-lm', '--load_model_path', type=str, dest='load_model_path', help='load_model_path', default='./tcn.pth')    
    parser.add_argument('-category', '--category', type=str, dest='category', help='use_ipex', default='ipex')   
    parser.add_argument('-config', '--config_path', type=str, dest='config_path', help='config_path', required=True)            
    args = parser.parse_args()
    return args

class TCNMetric(object):
  def __init__(self, *args):
      self.pred_list = []
      self.targets_list = []
      self.samples = 0
  def update(self, predict, targets):
      self.pred_list.extend(predict)
      self.targets_list.extend(targets)
      self.samples += len(targets)
  def reset(self):
      self.pred_list = []
      self.targets_list = []
      self.samples = 0
  def result(self):
      mse = np.mean(np.square(np.array([i.numpy() for i in self.pred_list]) - np.array([i.numpy() for i in self.targets_list])))      
      print('prediction shape', np.array([i.numpy() for i in self.pred_list]).shape)
      print('targets shape', np.array([i.numpy() for i in self.targets_list]).shape)
      print('MSE: ', mse)
      return mse

class TCNMetric_onnx(object):
  def __init__(self, *args):
      self.pred_list = []
      self.targets_list = []
      self.samples = 0
  def update(self, predict, targets):
      self.pred_list.extend(predict)
      self.targets_list.extend(targets)
      self.samples += len(targets)
  def reset(self):
      self.pred_list = []
      self.targets_list = []
      self.samples = 0
  def result(self):
      mse = np.mean(np.square(np.array([i for i in self.pred_list]) - np.array([i for i in self.targets_list])))      
      print('prediction shape', np.array([i for i in self.pred_list]).shape)
      print('targets shape', np.array([i for i in self.targets_list]).shape)
      print('MSE: ', mse)
      return mse

def preprocess_data(tx, ty, df, offset):
    trainx = df.iloc[offset:offset+tx, 3:5].values
    trainy = df.iloc[offset+tx:offset+tx+ty, 3:5].values
    return trainx, trainy

class AltranDataset_onnx(AltranDataset):
    def __len__(self):
        if self.mode == "train":
            return self.train_num
        if self.mode == "valid":
            return int(0.1*self.valid_num)
        if self.mode == "test":
            return int(0.1*self.test_num)
        return None

    def __getitem__(self, idx):

        offset = 0
        if self.mode == "valid":
            offset = self.train_num//8
        if self.mode == "test":
            offset = self.train_num//8 + self.valid_num//8
        
        df_num = idx%8
        idx = idx//8
        
        x, y = preprocess_data(tx=self.tx, ty=self.ty, df=self.df[df_num], offset=idx+offset)
        return x.astype(np.float32), y.astype(np.float32)

class AltranDataset_ipex(AltranDataset):
    def __len__(self):
        if self.mode == "train":
            return self.train_num
        if self.mode == "valid":
            return int(0.1*self.valid_num)
        if self.mode == "test":
            return int(0.1*self.test_num)
        return None

    def __getitem__(self, idx):

        offset = 0
        if self.mode == "valid":
            offset = self.train_num//8
        if self.mode == "test":
            offset = self.train_num//8 + self.valid_num//8
        
        df_num = idx%8
        idx = idx//8
        
        x, y = preprocess_data(tx=self.tx, ty=self.ty, df=self.df[df_num], offset=idx+offset)
        return x.astype(np.float32), y.astype(np.float32)        
  

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
    category = args.category
    config_path = args.config_path
    load_model_path = args.load_model_path

    input_size = 2
    num_channels = [hidden_units] * (levels-1) + [input_size]
    print(category)
    if category == 'ipex':
        print(category)
        import torch.fx.experimental.optimization as optimization
        from tcn_model import TemporalConvNet

        df = pd.read_csv(input_path)  
        dataset_valid = AltranDataset_ipex(df, mode="valid", tx=lookback, ty=horizon)

        model = TemporalConvNet(past_seq_len=lookback,
                feature_num=input_size, 
                future_seq_len=horizon, 
                num_channels=num_channels,
                dropout=dropout,
                kernel_size=kernel_size
                )          
        model.load_state_dict(torch.load(load_model_path, map_location=torch.device('cpu')))  
        # pytorch_model.eval()
        quantizer = Quantization(config_path)
        quantizer.metric = common.Metric(TCNMetric)
        quantizer.calib_dataloader = common.DataLoader(dataset_valid, batch_size=batch_size)
        quantizer.eval_dataloader = common.DataLoader(dataset_valid, batch_size=batch_size)
        quantizer.model = model
        q_model = quantizer()
        q_model.save('.') 

    elif category == 'onnx':
        from neural_compressor import options

        df = pd.read_csv(input_path)  
        dataset_valid_onnx = AltranDataset_onnx(df, mode="valid", tx=lookback, ty=horizon)
        options.onnxrt.graph_optimization.level = 'ENABLE_BASIC'
        quantizer = Quantization(config_path)
        quantizer.metric = common.Metric(TCNMetric_onnx)
        quantizer.model = common.Model(load_model_path)
        quantizer.calib_dataloader = common.DataLoader(dataset_valid_onnx, batch_size=batch_size)
        quantizer.eval_dataloader = common.DataLoader(dataset_valid_onnx, batch_size=batch_size)
        q_model = quantizer()
        q_model.save('tcn_int8.onnx')
if __name__ == '__main__':
    main()   