from kfp import dsl
from mlrun.platforms import auto_mount
import mlrun

funcs = {}

# init functions is used to configure function resources and local settings
def init_functions(functions: dict, project=None, secrets=None):
    for f in functions.values():
        f.apply(auto_mount())


@dsl.pipeline(
    name="Kando MLRun demo",
    description="Kando MLRun demo"
)
def kfpipeline():

    # run the ingestion function with the new image and params
    fetch = funcs['test'].as_step(
        name="fetch_data",
        handler='fetch_data',
        inputs={'dataset_url': "https://s3.wasabisys.com/iguazio/data/Taxi/taxi_zones.csv"},
        outputs=['test-dataset'])

    # Join and transform the data sets
    transform = funcs["test"].as_step(
        name="analyze_data",
        handler='analyze_data',
        inputs={"dataset": fetch.outputs['test-dataset']},
        outputs=['result'])
