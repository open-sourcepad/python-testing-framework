from selenium import webdriver
from seleniumrequests import Firefox
from selenium.webdriver.firefox.options import Options
from seleniumrequests.request import headers

class SeleniumError(Exception):
    pass

class Selenium:
    def __init__(self, **kwargs):
        self.method = kwargs.get('method', 'get')
        self.data = kwargs.get('data')
        self.headers = kwargs.get('headers')
        self.options = Options()
        self._options()

    def browser(self, url):
        try:
            driver = Firefox(options=self.options)
            headers = self.headers
            result = driver.request(self.method, url, data=self.data)
            import pry;pry()
            return driver
        except Exception as e:
            raise SeleniumError(f"Error setting instance of Firefox.\nError: {e}")

    def _options(self):
        self.options.headless = True
