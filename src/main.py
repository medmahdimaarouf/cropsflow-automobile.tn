import asyncio

from cropsflow import CropsFlow
from cropsflow.orchestrator import Worker

from app_module import AppModule
from src.tasks import LoadBrandsTask, LoadVersionsTask, LoadModelsTask


async def start():
    app = await CropsFlow.start(AppModule)
    worker: Worker = app.get_orchestrator().create_worker(LoadModelsTask)
    worker.start()


if __name__ == '__main__':
    asyncio.run(start())
