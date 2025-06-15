from cropsflow.common.decorators import task


@task(template_path='../../templates/tasks/load_brands_task.xml')
class LoadBrandsTask:
    pass
