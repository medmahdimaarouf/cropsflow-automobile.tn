from cropsflow.common.decorators import task


@task(template_path='../../templates/tasks/load_versions_task.xml')
class LoadVersionsTask:
    pass
