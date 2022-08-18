# dataldr.py
import sys
import torch
from torch.utils.data import Dataset, DataLoader
import logging
import time

import pandas as pd
import numpy as np

def preprocess_data(tx, ty, df, offset):
    trainx = df.iloc[offset:offset+tx, 3:5].values
    trainy = df.iloc[offset+tx:offset+tx+ty, 3:5].values
    return trainx, trainy

class AltranDataset(Dataset):
    """AltranDataset"""

    def __init__(self, df, mode="train", tx=80, ty=40):
        
        assert mode in ["train", "valid", "test"]

        self.mode = mode
        self.tx = tx
        self.ty = ty

        df = df[["timestamp", "tick", "ue", "currentCQI_cw1", "currentCQI_cw2"]]
        df0 = df[df["ue"]==0]
        df1 = df[df["ue"]==1]
        df2 = df[df["ue"]==2]
        df3 = df[df["ue"]==3]
        df4 = df[df["ue"]==4]
        df5 = df[df["ue"]==5]
        df6 = df[df["ue"]==6]
        df7 = df[df["ue"]==7]

        self.df = [df0, df1, df2, df3, df4, df5, df6, df7]

        self.train_num = int(0.8*(len(df0)-tx-ty+1))
        self.valid_num = int(0.1*(len(df0)-tx-ty+1))
        self.test_num = (len(df0) - tx - ty + 1 - self.train_num - self.valid_num)

        self.train_num *= 8
        self.valid_num *= 8
        self.test_num *= 8

        print("---------------------------")
        print("Altran Dataset is created!")
        print("Dataset Overiew:")
        print("---------------------------")
        print("tx:", self.tx)
        print("ty:", self.ty)
        print("mode:", self.mode)
        if self.mode == "train":
            print("trian_num:", self.train_num) 
        if self.mode == "valid":
            print("valid_num:", self.valid_num)
        if self.mode == "test":
            print("test_num:", self.test_num)
        print("---------------------------")

    def __len__(self):
        if self.mode == "train":
            return self.train_num
        if self.mode == "valid":
            return self.valid_num
        if self.mode == "test":
            return self.test_num
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
        x = torch.from_numpy(x).type(torch.float)
        y = torch.from_numpy(y).type(torch.float)
        return x, y
