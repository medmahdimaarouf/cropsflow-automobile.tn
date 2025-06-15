from cropsflow.common.decorators import task


@task(template_path='../../templates/load_brands_task.xml')
class LoadBrandsTask:
    pass
