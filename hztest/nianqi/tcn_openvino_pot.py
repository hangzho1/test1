# tcn_openvino_pot.py 
# Copyright 2020 Intel Corporation.
#
# This software and the related documents are Intel copyrighted materials,
# and your use of them is governed by the express license under which they
# were provided to you (End User License Agreement for the Intel(R) Software
# Development Products (Version October 2018)). Unless the License provides
# otherwise, you may not use, modify, copy, publish, distribute, disclose or
# transmit this software or the related documents without Intel's prior
# written permission.
#
# This software and the related documents are provided as is, with no
# express or implied warranties, other than those that are expressly
# stated in the License.

from dataldr import AltranDataset
import argparse
import os
import hashlib
import numpy as np
import pandas as pd
from tqdm import tqdm
from addict import Dict
from sklearn.metrics import mean_squared_error

from compression.api import Metric, DataLoader
from compression.graph import load_model, save_model
from compression.graph.model_utils import compress_model_weights
from compression.engines.ie_engine import IEEngine
from compression.pipeline.initializer import create_pipeline
from compression.utils.logger import init_logger

# Initialize the logger to print the quantization process in the console.
init_logger(level='INFO')


# Custom DataLoader class implementation that is required for
# the proper reading of Imagenet images and annotations.
class TCNDataLoader(DataLoader):

    def __init__(self, config):
        if not isinstance(config, Dict):
            config = Dict(config)
        super().__init__(config)
        df = pd.read_csv(config['data_source'])
        self._annotations = {}
        self._input_datas = {}
        self._data_idx = []
        self._dataset = AltranDataset(df, mode=config['mode'], 
                tx=int(config['input_time_step']), ty=int(config['output_time_step']))
        self._check_md5sum = config.get('fast_check_md5sum', False)
        print("Reading TCN dataset ....")
        self._read_tcn_data()
        print("Loaded TCN dataset successfully.")

    def __len__(self):
        if self._check_md5sum:
            return 4
        else:
            return len(self._dataset)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        if index not in self._annotations or index not in self._input_datas:
            raise IndexError

        annotation = (index, self._annotations[index])
        input_data = self._input_datas[index]
        return annotation, input_data

    # Methods specific to the current implementation
    def _read_tcn_data(self):
        x, y = 0, 1
        for i in tqdm(range(len(self))):
            if i in self._annotations or i in self._input_datas:
                raise IndexError
            self._annotations[i] = self._dataset[i][y].numpy()
            self._input_datas[i] = self._dataset[i][x].numpy()
            self._data_idx.append(i)

# Custom implementation of classification accuracy metric.
class MeanSquaredError(Metric):

    # Required methods
    def __init__(self, metric_config, check=False):
        super().__init__()
        self._mse = []
        self._check_md5sum = check
        self._metric_config = metric_config
        if self._metric_config == 'MSE':
            self._name = 'Mean Squared Error'
        elif self._metric_config == 'RMSE':
            self._name = 'Root Mean Squared Error'
        else:
            raise ValueError("not defined value metric!")

    @property
    def value(self):
        """ Returns accuracy metric value for the last model output. """
        return {self._name: np.array([self._mse[-1]])} 

    @property
    def avg_value(self):
        """ Returns accuracy metric value for all model outputs. """
        if self._check_md5sum:
            md5sum = hashlib.md5(np.array(self._mse)).hexdigest()
        if self._metric_config == 'MSE':
            return {self._name: np.mean(self._mse)}
        elif self._metric_config == 'RMSE':
            return {self._name: np.sqrt(np.mean(self._mse))}
        else:
            raise ValueError("not defined value metric!")

    def update(self, output, target):
        """ Updates prediction matches.
        :param output: model output
        :param target: annotations
        """
        if len(output) > 1:
            raise Exception('The accuracy metric cannot be calculated '
                            'for a model with multiple outputs')
        if isinstance(target, dict):
            target = list(target.values())
        mse = mean_squared_error(target[0], output[0].squeeze())
        self._mse.append(mse)

    def reset(self):
        """ Resets collected matches """
        self._mse = []

    def get_attributes(self):
        """
        Returns a dictionary of metric attributes {metric_name: {attribute_name: value}}.
        Required attributes: 'direction': 'higher-better' or 'higher-worse'
                             'type': metric type
        """
        return {self._name: {'direction': 'higher-worse',
                             'type': 'accuracy'}}


def get_configs(args):
    if 'weights' not in args:
        args['weights'] = '{}.bin'.format(os.path.splitext(args['model'])[0])

    model_config = Dict({
        'model_name': 'tcn',
        'model': args['model'],
        'weights': args['weights']
    })
    engine_config = Dict({
        'device': 'CPU',
        'stat_requests_number': 2,
        'eval_requests_number': 2
    })
    dataset_config = {
        'data_source': args['dataset'],
        'mode': args['mode'],
        'input_time_step': args['input_time_step'],
        'output_time_step': args['output_time_step'],
        'fast_check_md5sum': args.get('fast_check_md5sum', False),
    }
    algorithms = [{
        'name': 'DefaultQuantization',
        'params': {
            'target_device': 'CPU',
            'preset': 'performance',
            'stat_subset_size': 300
        }
    }]


    metric_config = args['metric_config']
    return model_config, engine_config, dataset_config, algorithms, metric_config


def optimize_model(args):
    model_config, engine_config, dataset_config, algorithms, metric_config = get_configs(args)

    # Step 1: Load the model.
    model = load_model(model_config)

    # Step 2: Initialize the data loader.
    data_loader = TCNDataLoader(dataset_config)

    # Step 3 (Optional. Required for AccuracyAwareQuantization): Initialize the metric.
    metric = MeanSquaredError(metric_config)

    # Step 4: Initialize the engine for metric calculation and statistics collection.
    engine = IEEngine(engine_config, data_loader, metric)

    # Step 5: Create a pipeline of compression algorithms.
    pipeline = create_pipeline(algorithms, engine)
    
    # Step 6: Execute the pipeline.
    compressed_model = pipeline.run(model)

    # Step 7 (Optional): Compress model weights quantized precision
    #                    in order to reduce the size of final .bin file.
    compress_model_weights(compressed_model)

    return compressed_model, pipeline

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', type=str, dest='input_path', help='input dataset path', default="stats_ue.csv")
    parser.add_argument('-xml', '--network_xml', type=str, dest='network_xml', help='network xml file', default='model/xml/tcn.xml')
    parser.add_argument('-l', '--lookback', type=int, dest='lookback', help='lookback', default=320)
    parser.add_argument('-o', '--horizon', type=int, dest='horizon', help='horizon', default=40)
    parser.add_argument('-sm', '--save_model_path', type=str, dest='save_model_path', help='save_model_path', default='int8/')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    input_path = args.input_path
    network_xml = args.network_xml
    lookback = args.lookback
    horizon = args.horizon 
    save_model_path = args.save_model_path
    print("\nOPENVINO INT8 LATENCY & MSE IS BELOW:")
    kwargs = {
        "model": network_xml,
        "dataset": input_path,
        "mode": "test",
        "input_time_step": lookback,
        "output_time_step": horizon,
        "fast_check_md5sum": False, # use for bitmatch check after optimization
        "metric_config": 'MSE', # RMSE or MSE
    }

    # Steps 1-7: Model optimization
    compressed_model, pipeline = optimize_model(kwargs)

    # Step 8: Save the compressed model to the desired path.
    save_model(compressed_model, save_model_path)
    
    # Step 9 (Optional): Evaluate the compressed model. Print the results.
    #metric_results = pipeline.evaluate(compressed_model)
    #if metric_results:
    #    for name, value in metric_results.items():
    #        print('{: <27s}: {}'.format(name, value))


if __name__ == '__main__':
    main()
