from libs.csv_reader import CsvReader
from .base import CallBackBase

class Sample(CallBackBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method = 'get'
        # self.json = self._set_json()
        # self.headers = self._set_headers()
        # self.data = self._set_data()
        self.url_endpoint = f"{self.test_url}"

    def run(self):
        result = self.visit_url(self.url_endpoint)
        self.test_result = result.status_code == 400
        super().run()
        return result

    # def _set_json(self):
    #     return {}

    # def _set_headers(self):
    #     return {}

    # def _set_data(self):
    #     return {}
