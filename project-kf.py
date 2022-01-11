from os import path
from mlrun import auto_mount
from nuclio.triggers import V3IOStreamTrigger, CronTrigger
import mlrun

# Create project.yaml
project_name_base = 'test-mlrun'

project_path = path.abspath('.')
project = mlrun.new_project(project_name_base,
                            context=project_path)

project.set_function(f'db://{project.name}/test')

project.set_workflow('main', 'workflow.py', embed=True)

# This will create the YAML file locally
project.save()

# ======================================================================================================
# Now upload, by code or manually, the YAML to V3IO /User/remote-project/project.yaml
# ======================================================================================================

# Create Nuclio function to trigger the pipeline
pipline_trigger_fun = mlrun.code_to_function("pipeline-trigger",
                                             project_name_base,
                                             kind="nuclio",
                                             filename="pipeline-trigger.py",
                                             image="mlrun/mlrun")

pipline_trigger_fun.apply(auto_mount())

pipline_trigger_fun.add_trigger('cron', CronTrigger(schedule="0 8 * * *"))

pipline_trigger_fun.deploy()