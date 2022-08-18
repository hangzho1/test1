# tcn_chronos.py
import numpy as np
import tempfile
import os
import torch
import pandas as pd
from bigdl.chronos.forecaster import TCNForecaster
from bigdl.chronos.data import TSDataset
import argparse
from dataldr import AltranDataset
from torch.utils.data import DataLoader
from time import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', type=str, dest='input_path', help='input dataset path', default="stats_ue.csv")
    parser.add_argument('-vr', '--val_ratio', type=float, dest='val_ratio', help='validation ratio', default=0.1)
    parser.add_argument('-tr', '--test_ratio', type=float, dest='test_ratio', help='test ratio', default=0.1)
    parser.add_argument('-l', '--lookback', type=int, dest='lookback', help='lookback', default=320)
    parser.add_argument('-o', '--horizon', type=int, dest='horizon', help='horizon', default=40)
    parser.add_argument('-b', '--batch_size', type=int, dest='batch_size', help='batch_size', default=512)
    parser.add_argument('-ls', '--levels', type=int, dest='levels', help='levels', default=8)
    parser.add_argument('-hu', '--hidden_units', type=int, dest='hidden_units', help='hidden_units', default=48)
    parser.add_argument('-k', '--kernel_size', type=int, dest='kernel_size', help='kernel_size', default=3)
    parser.add_argument('-d', '--dropout', type=float, dest='dropout', help='dropout', default=0.1)
    parser.add_argument('-lr', '--learning_rate', type=float, dest='learning_rate', help='learning_rate', default=0.001)
    parser.add_argument('-e', '--epochs', type=int, dest='epochs', help='epochs', default=1)
    parser.add_argument('-m', '--mode', type=str, dest='mode', help='training or inference mode', default='train')
    parser.add_argument('-sm', '--save_model_path', type=str, dest='save_model_path', help='save_model_path', default='.')
    parser.add_argument('-lm', '--load_model_path', type=str, dest='load_model_path', help='load_model_path', default='.')

    args = parser.parse_args()

    return args

def main():    

    args = parse_args()
    input_path = args.input_path
    val_ratio = args.val_ratio
    test_ratio = args.test_ratio
    lookback = args.lookback
    horizon = args.horizon
    batch_size = args.batch_size
    levels = args.levels
    hidden_units = args.hidden_units
    kernel_size = args.kernel_size
    dropout = args.dropout
    learning_rate = args.learning_rate
    epochs = args.epochs
    mode = args.mode
    save_model_path = args.save_model_path
    load_model_path = args.load_model_path
    input_size = 2
    num_channels = [hidden_units] * (levels-1)

    df = pd.read_csv(input_path)

    if mode.lower() == 'train':
        start_time = time()
        tsdata_train, tsdata_valid, tsdata_test = TSDataset.from_pandas(df,
                                                                    dt_col="timestamp",
                                                                    id_col="ue",
                                                                    target_col=["currentCQI_cw1", "currentCQI_cw2"],
                                                                    with_split=True,
                                                                    val_ratio=val_ratio,
                                                                    test_ratio=test_ratio)

        for tsdata in [tsdata_train, tsdata_valid, tsdata_test]:
            tsdata.roll(lookback=lookback, horizon=horizon)

        x_train, y_train = tsdata_train.to_numpy()
        x_val, y_val = tsdata_valid.to_numpy()
        x_test, y_test = tsdata_test.to_numpy()

        print("train sample num:", x_train.shape[0])
        print("test sample num:", x_test.shape[0])



        forecaster = TCNForecaster(past_seq_len=lookback,
                                    future_seq_len=horizon,
                                    input_feature_num=input_size,
                                    output_feature_num=input_size,
                                    kernel_size=kernel_size,
                                    num_channels=num_channels,
                                    loss="mse",
                                    metrics=['mse'],
                                    lr=learning_rate,
                                    dropout=dropout,
                                    distributed=False,
                                    seed=5)

        forecaster.fit(data=(x_train, y_train),
                epochs=epochs,
                batch_size=batch_size//forecaster.num_processes)  # please revice this as benchmark plan asks

        print("training_whole time(alternative): ", time() - start_time, "s")

        forecaster.save(save_model_path)
        forecaster.load(save_model_path) 

        result = forecaster.evaluate(data=(x_test, y_test),
                                multioutput='uniform_average')
        print(f'MSE for test dataset: {result}')

    elif mode.lower() == 'inference':
        # load and predict
        os.environ['OMP_NUM_THREADS'] = "1"  # for inferencing, we use 1 thread
        torch.set_num_threads(1) # for inferencing, we use 1 thread
        tsdata_train, tsdata_valid, tsdata_test = TSDataset.from_pandas(df,
                                                                    dt_col="timestamp",
                                                                    id_col="ue",
                                                                    target_col=["currentCQI_cw1", "currentCQI_cw2"],
                                                                    with_split=True,
                                                                    val_ratio=0.1,
                                                                    test_ratio=0.1)

        for tsdata in [tsdata_train, tsdata_valid, tsdata_test]:
            tsdata.roll(lookback=lookback, horizon=horizon)

        x_train, y_train = tsdata_train.to_numpy()
        x_val, y_val = tsdata_valid.to_numpy()
        x_test, y_test = tsdata_test.to_numpy()

        forecaster = TCNForecaster(past_seq_len=lookback,
                                    future_seq_len=horizon,
                                    input_feature_num=input_size,
                                    output_feature_num=input_size,
                                    kernel_size=kernel_size,
                                    num_channels=num_channels,
                                    loss="mse",
                                    metrics=['mse'],
                                    lr=learning_rate,
                                    dropout=dropout,
                                    distributed=False,
                                    seed=5)
        forecaster.load(load_model_path)
        
        # test mse first
        print('-------- Start to check mse from Chronos Evaluator --------')
        result = forecaster.evaluate(data=(x_test, y_test),
                                multioutput='uniform_average')
        print(f'Chronos test mse: {result}')

        warmup_data = 100
        data_length = x_test.shape[0]
        data_length_inference = data_length - warmup_data

        # default prediction
        mse = 0
        time_test_diff = 0
        for index in range(data_length):
            if index < warmup_data:
                time_test_diff = 0
            x, y_hat  = np.expand_dims(x_test[index], axis=0), np.expand_dims(y_test[index], axis=0)
            time_test_start = time()
            y_pred = forecaster.predict(x)
            time_test_end = time()
            time_test_diff = time_test_diff + (time_test_end - time_test_start)
            mse = mse + np.sum(np.square(y_hat - y_pred))
        latency = (time_test_diff*1000)/data_length_inference
        throughput = data_length_inference/time_test_diff
        mse = mse/(data_length_inference*horizon*input_size)
        print('-------- Default Predict Process --------')
        print('Data Length: {data_shape}'.format(data_shape=data_length_inference))
        print('chronos pytorch Latency (ms): {latency} \nchronos pytorch Throughput (item/s): {throughput} \nchronos pytorch MSE: {mse}'.format(latency=latency,
                                                                                throughput=throughput,
                                                                                mse=mse))

        # onnx prediction
        forecaster.build_onnx(thread_num=1)
        mse = 0
        time_test_diff = 0
        for index in range(data_length):
            if index < warmup_data:
                time_test_diff = 0
            x, y_hat  = np.expand_dims(x_test[index], axis=0), np.expand_dims(y_test[index], axis=0)
            time_test_start = time()
            y_pred = forecaster.predict_with_onnx(x)
            time_test_end = time()
            time_test_diff = time_test_diff + (time_test_end - time_test_start)
            mse = mse + np.sum(np.square(y_hat - y_pred))
        latency = (time_test_diff*1000)/data_length_inference
        throughput = data_length_inference/time_test_diff
        mse = mse/(data_length_inference*horizon*input_size)
        print('-------- Default Predict Process --------')
        print('Data Length: {data_shape}'.format(data_shape=data_length_inference))
        print('chronos onnx Latency (ms): {latency} \nchronos onnx Throughput (item/s): {throughput} \nchronos onnx MSE: {mse}'.format(latency=latency,
                                                                                throughput=throughput,
                                                                                mse=mse))


        # ipex prediction
        print('Check and open the use_ipex flag:')
        print(forecaster.use_ipex)
        forecaster.use_ipex = True
        print(forecaster.use_ipex)
        mse = 0
        time_test_diff = 0
        for index in range(data_length):
            if index < warmup_data:
                time_test_diff = 0
            x, y_hat  = np.expand_dims(x_test[index], axis=0), np.expand_dims(y_test[index], axis=0)
            time_test_start = time()
            y_pred = forecaster.predict(x)
            time_test_end = time()
            time_test_diff = time_test_diff + (time_test_end - time_test_start)
            mse = mse + np.sum(np.square(y_hat - y_pred))
        latency = (time_test_diff*1000)/data_length_inference
        throughput = data_length_inference/time_test_diff
        mse = mse/(data_length_inference*horizon*input_size)
        print('-------- Default Predict Process --------')
        print('Data Length: {data_shape}'.format(data_shape=data_length_inference))
        print('chronos ipex Latency (ms): {latency} \nchronos ipex Throughput (item/s): {throughput} \nchronos ipex MSE: {mse}'.format(latency=latency,
                                                                                throughput=throughput,
                                                                                mse=mse))

if __name__ == '__main__':
    main()
