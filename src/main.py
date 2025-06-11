import asyncio

from cropsflow import CropsFlow
from cropsflow.orchestrator import Worker

from app_module import AppModule
from prix_de_neuf_task import PrixDeNeufTask


async def start():
    app = await CropsFlow.start(AppModule)
    worker: Worker = app.get_orchestrator().create_worker(PrixDeNeufTask)
    worker.start()


if __name__ == '__main__':
    asyncio.run(start())
