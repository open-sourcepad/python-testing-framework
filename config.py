import yaml
from pathlib import Path

from peewee import *
from playhouse.pool import PooledMySQLDatabase
from helpers.typecast_helper import to_int

class Config:
    def __init__(self, file='app'):
        pwd = str(Path(__file__).parent)
        with open(f"{ pwd }/configs/{ file }.yml") as stream:
            try:
                data = yaml.safe_load(stream)
                self.data = data[data['default']['environment']]
            except Exception as e:
                print(e)

    @classmethod
    def default_imports(self):
        result = {}
        for module in ['pry']:
            result[module] = __import__(module)
        return result

    @property
    def get_all(self):
        return self.data

    def get(self, key):
        return self.get_all[key]

class Database:
    def __init__(self):
        self.config = Config(file='database').get_all
        self.database = self.config['database']
        self.db_config = {}

        for attr in self._attributes:
            self.db_config[attr] = to_int(self.config[attr])

    @property
    def instance(self):
        return MySQLDatabase(
            self.database,
            **self.db_config
        )

    @property
    def _attributes(self):
        return [
            'user',
            'password',
            'host',
            'port'
        ]
