from selenium import webdriver
from seleniumrequests import Firefox
from selenium.webdriver.firefox.options import Options
from seleniumrequests.request import headers

class SeleniumError(Exception):
    pass

class Selenium:
    def __init__(self, **kwargs):
        self.options = Options()
        self._options()

    def browser(self, url):
        try:
            driver = Firefox(options=self.options)
            driver.get(url)

            return driver
        except Exception as e:
            raise SeleniumUatError(f"Error setting instance of Firefox.\nError: {e}")

    def _options(self):
        self.options.headless = True
