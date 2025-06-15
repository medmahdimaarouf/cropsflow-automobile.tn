from cropsflow_dom import DOMModule
from cropsflow_mongo import MongoModule
from cropsflow.common.decorators import module
from cropsflow.common import CommonModule

from cropsflow_http import HttpModule
from prix_de_neuf_task import PrixDeNeufTask
from src.pipes import PricePipe
from src.tasks import LoadBrandsTask, LoadVersionsTask, LoadModelsTask


@module(
    declarations=[
        PrixDeNeufTask,
        LoadBrandsTask,
        LoadVersionsTask,
        LoadModelsTask,
        PricePipe
    ],
    imports=[
        CommonModule,
        MongoModule.register(
            uri='mongodb://localhost:27017',
            db_name='prx-automobile-tn-2'
        ),
        HttpModule,
        DOMModule
    ],
    providers=[

    ]
)
class AppModule:
    pass
