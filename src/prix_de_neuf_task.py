from cropsflow.common.decorators import task


@task(template_path='../templates/prix_de_neuf.task.xml')
class PrixDeNeufTask:
    pass
