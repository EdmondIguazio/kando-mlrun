from mlrun.execution import MLClientCtx
from mlrun.datastore import DataItem
from os import path
import pickle5 as pickle
from myclass import EdmondTestClass

def train_model(context: MLClientCtx):
    c = EdmondTestClass()
    p = pickle.dumps(c)
    

def fetch_data(context: MLClientCtx, dataset_url: DataItem):

    context.logger.info('Reading data from {}'.format(dataset_url))
    dataset_df = dataset_url.as_df()

    target_path = path.join(context.artifact_path, 'data')

    # Store the data sets in your artifacts database
    context.log_dataset('test-dataset', df=dataset_df, format='parquet',
                        index=False, artifact_path=target_path)


def analyze_data(context: MLClientCtx, dataset: DataItem):

    dataset_df = dataset.as_df()

    target_path = path.join(context.artifact_path, 'data')

    size = dataset_df.size

    context.logger.info(f"DF size is {size}")

    # Store the data sets in your artifacts database
    context.log_result("result", size)
