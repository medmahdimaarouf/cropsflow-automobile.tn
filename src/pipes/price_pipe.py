from typing import Dict, Any

from cropsflow import TaskContext, D
from cropsflow.common import Pipe
from cropsflow.common.decorators import pipe


@pipe(selector="pipe-price")
class PricePipe(Pipe):

    def __init__(self):
        super().__init__(data=0)

    def accumulate(self, context: TaskContext, options: Dict[str, Any] = {}, data: D = None,
                   accessor: str = None) -> None:
        self.set_data(0)
