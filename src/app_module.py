from cropsflow_dom import DOMModule
from cropsflow_mongo import MongoModule
from cropsflow.common.decorators import module
from cropsflow.common import CommonModule

from cropsflow_http import HttpModule
from src.tasks import LoadBrandsTask, LoadVersionsTask, LoadModelsTask


@module(
    declarations=[
        LoadBrandsTask,
        LoadVersionsTask,
        LoadModelsTask,
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
