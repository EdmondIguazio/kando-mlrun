# This is a sample Python script.
import mlrun
from mlrun.platforms import auto_mount

project_name_base = 'test-mlrun'

project_name, artifact_path = mlrun.set_environment(project=project_name_base)

print(f'Project name: {project_name}')
print(f'Artifact path: {artifact_path}')

test_func = mlrun.code_to_function(name='test',
                                   filename= 'step.py',
                                   kind='job',
                                   image='mlrun/mlrun')
test_func.apply(auto_mount())

fetch_data_run = test_func.run(name='step_one',
                               handler='fetch_data',
                               inputs={'dataset_url': 'https://s3.wasabisys.com/iguazio/data/Taxi/taxi_zones.csv'})