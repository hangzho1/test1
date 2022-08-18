# tcn_openvino_mse.py  
import argparse
import os
from compression.graph import load_model
from compression.engines.ie_engine import IEEngine
from tcn_openvino_pot import TCNDataLoader, MeanSquaredError, get_configs



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', type=str, dest='input_path', help='input dataset path', default="stats_ue.csv")
    parser.add_argument('-xml', '--network_xml', type=str, dest='network_xml', help='network xml file', default="model/xml/tcn.xml")
    parser.add_argument('-l', '--lookback', type=int, dest='lookback', help='lookback', default=320)
    parser.add_argument('-o', '--horizon', type=int, dest='horizon', help='horizon', default=40)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    input_path = args.input_path
    network_xml = args.network_xml
    lookback = args.lookback
    horizon = args.horizon 

    kwargs = {
        "model": network_xml,
        "dataset": input_path,
        "mode": "test",
        "input_time_step": lookback,
        "output_time_step": horizon,
        "fast_check_md5sum": False,
        "metric_config": 'MSE'
    }

    model_config, engine_config, dataset_config, _, _ = get_configs(kwargs)

    # Step 1: Load the model.
    model = load_model(model_config)

    # Step 2: Initialize the data loader.
    data_loader = TCNDataLoader(dataset_config)

    # Step 3 (Optional. Required for AccuracyAwareQuantization): Initialize the metric.
    metric = MeanSquaredError(kwargs['metric_config'], kwargs['fast_check_md5sum'])

    # Step 4: Initialize the engine for metric calculation and statistics collection.
    engine = IEEngine(engine_config, data_loader, metric)

    # Step 5 (Optional): Evaluate the model. Print the results.
    engine.calculate_metrics = True
    engine.set_model(model)
    metrics, _ = engine.predict(print_progress=True)
    if metrics:
        for name, value in metrics.items():
            print('{: >17s}: {}'.format(name, value))


if __name__ == '__main__':
    main()
