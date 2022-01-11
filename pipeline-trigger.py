from mlrun import load_project

project_pipeline = load_project(context='/User/remote-project',
                                url='/User/remote-project/project.yaml',
                                name='remote-project')

def handler(context, event):
    context.logger.info('Triggering pipeline')

    run_id = project_pipeline.run(name='main',
                                  dirty=True)

    return context.Response(body=f'Pipeline triggered, run id: {run_id}',
                            headers={},
                            content_type='text/plain',
                            status_code=200)
