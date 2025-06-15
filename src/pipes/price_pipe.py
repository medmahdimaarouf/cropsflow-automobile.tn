from typing import Dict, Any

from cropsflow.common import Pipe
from cropsflow.common.decorators import pipe


@pipe(selector="pipe-price")
class PricePipe(Pipe):

    def __init__(self):
        super().__init__(data=0)

    def transform(self, data: any = None, options: Dict[str, Any] = None) -> None:
        self._data = 0
