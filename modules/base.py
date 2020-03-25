import unittest
from libs.selenium import Selenium
from config import Config
from libs.callback import Callback

class Base:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.test_url = Config().get('test_url')
        self.print_results = kwargs.get('print_results', True)
        self.url_endpoint = ''

    def run(self):
        if self.print_results:
            print('===========================================================')
            print(f"Running endpoint: {self.url_endpoint}")
            print(f"{self.__class__.__name__} Passed: {self.test_result}")
            print('===========================================================')

class SeleniumBase(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.method = 'get'
        self.browser_name = 'Firefox'
        self.data = self._set_params()
        self.headers = self._set_headers()

    def visit_url(self, url):
        args = {
            'method': self.method,
            'data': self.data,
            'headers': self.headers
        }
        result = Selenium(**args).browser(url)

        return result

class CallBackBase(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method = 'get'

        for arg in ['data', 'json', 'headers']:
            setattr(self, arg, {})

    def visit_url(self, url):
        return Callback(
            url=url,
            method=self.method,
            data=self.data,
            json=self.json,
            headers=self.headers
        ).request()

class UnitTestBase(Base, unittest.TestCase):
    pass
