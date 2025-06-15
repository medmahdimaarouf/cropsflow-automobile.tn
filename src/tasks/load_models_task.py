from cropsflow.common.decorators import task


@task(template_path='../../templates/tasks/load_models_task.xml')
class LoadModelsTask:
    pass
