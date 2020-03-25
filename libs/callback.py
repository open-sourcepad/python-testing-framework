import requests
from .logger import Logger

class Callback:
    def __init__(self, method='post', url='', data={}, json={}, headers={}):
        self.req = getattr(requests, method)
        self.url = url
        self.data = data
        self.json = json
        self.headers = headers

    def request(self):
        try:
            result = self.req(self.url, data=self.data, json=self.json, headers=self.headers)

            return result
        except Exception as e:
            Logger(file='callback', message=str(e), type='error').log()
            return e
