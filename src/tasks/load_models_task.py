from cropsflow.common.decorators import task


@task(template_path='../../templates/load_models_task.xml')
class LoadModelsTask:
    pass
