from config import Config
from procedures import Procedures
from middleware import *

class Main:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self._middleware()

    # test kwargs is required
    def run(self):
        return Procedures(**self.kwargs).run()

    def run_all(self):
        return Procedures(**self.kwargs).run_all()

    def _middleware(self):
        for middleware in self.kwargs['middleware']:
            middleware()


middleware = [
    Db
]

if __name__ == "__main__":
    configs = Config.default_imports()
    configs['middleware'] = middleware
    Main(**configs).run_all()
