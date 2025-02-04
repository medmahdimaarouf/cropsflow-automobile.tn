import asyncio

from cropsflow import CropsFlow

from cropsflow_dom import DOMModule
from cropsflow_mongo import MongoModule
from cropsflow.common.decorators import module
from cropsflow.common import CommonModule

from cropsflow_http import HttpModule
from prix_de_neuf_task import PrixDeNeufTask


@module(
    declarations=[
        PrixDeNeufTask
    ],
    imports=[
        CommonModule,
        MongoModule.register(
            uri='mongodb://localhost:27017',
            db_name='prx-automobile-tn'
        ),
        HttpModule,
        DOMModule
    ]
)
class AppModule:
    pass


async def start():
    app = await CropsFlow.start(AppModule)


if __name__ == '__main__':
    asyncio.run(start())
