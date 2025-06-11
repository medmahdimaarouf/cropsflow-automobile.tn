from cropsflow.common import Pipe
from cropsflow.common.decorators import pipe


@pipe(selector="pipe-price")
class PricePipe(Pipe):

    def __init__(self):
        self.set_data(data='')

    def accumulate(self, data: str) -> None:
        pass
