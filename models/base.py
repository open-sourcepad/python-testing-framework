# -*- coding: utf-8 -*-

from peewee import *
from config import Database as DB
from datetime import datetime as DT
from decimal import Decimal

class Base(Model):
    class Meta:
        database = DB().instance

    def get_all_keys(self):
        return list(self._meta.fields.keys())

    def get_data(self, **kwargs):
        result = {}
        whitelist = kwargs.get('keys')
        serializable = kwargs.get('serializable')

        for k,v in self.__data__.items():
            if whitelist and k not in whitelist:
                next
            elif serializable and type(v) in (DT, Decimal):
                result[k] = str(v)
            else:
                result[k] = v

        return result

    def get_filtered_data(self, serializable=False):
        return self.get_data(serializable=serializable)

    def get_data_except(self, keys = {}, serializable=False):
        raw_data = self.get_data(serializable=serializable)
        return { x: raw_data[x] for x in raw_data if x not in keys }

    def reload(self):
        return type(self).get_by_id(self._pk)

    @classmethod
    def first(self):
        return self.select().first()

    @classmethod
    def last(self):
        return self.select().sort(column='id', order='desc').first()

    @classmethod
    def find_by(cls, column, value):
        return cls.select().where(getattr(cls, column)==value).first()
