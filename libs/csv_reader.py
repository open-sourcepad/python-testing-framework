import csv
from pathlib import Path
from config import Config
from .logger import Logger

class CsvReader:
    def __init__(self, **kwargs):
        self.config = Config()
        pwd = self.config.get('root_url')
        file = f"{ pwd }"
        self.file = f"{ pwd }/assets/{kwargs.get('file')}.csv"

    def read(self):
        result = []
        with open(self.file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result.append(dict(row))

        Logger(file='test', message=result, type='info').log()
        return result
