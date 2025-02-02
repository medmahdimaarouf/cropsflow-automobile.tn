from cropsflow_dom import DOMModule
from cropsflow_mongo import MongoModule
from cropsflow.common import module, CommonModule

from prix_de_neuf_task import PrixDeNeufTask
from cropsflow_http import HttpModule


@module(
    delarations=[
        PrixDeNeufTask
    ],
    imports=[
        CommonModule,
        MongoModule.register(
            uri='mongodb://app-master:tCJIcCbF5r3lQWk4@ac-xjeanjg-shard-00-00.tljeoq9.mongodb.net:27017,'
                'ac-xjeanjg-shard-00-01.tljeoq9.mongodb.net:27017,'
                'ac-xjeanjg-shard-00-02.tljeoq9.mongodb.net:27017/?ssl=true&replicaSet=atlas-isac7m-shard-0'
                '&authSource=admin&retryWrites=true&w=majority&appName=Cluster0',
            db_name='prx-automobile-tn'
        ),
        HttpModule,
        DOMModule
    ]
)
class AppModule:
    pass
