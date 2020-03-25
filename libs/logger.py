import os, logging
from logging.handlers import RotatingFileHandler

class Logger:

    def __init__(self, **kwargs):
        self.info_format = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
        self.timestamp_format = '%Y-%m-%d %H:%M:%S %z'
        self.message = kwargs['message']
        self.type = 'info'
        self.file = 'app'

        if 'type' in kwargs.keys():
            self.type = kwargs['type']

        if 'file' in kwargs.keys():
            self.file = kwargs['file']

    def log(self):
        log = self._log()
        log.handlers.clear()
        log.addHandler(self._file_handler())
        log.setLevel(getattr(logging, self.type.upper()))
        return getattr(log, self.type)(self.message)

    def _log(self):
        return logging.getLogger(self.file)

    def _file_handler(self):
        calc = 1 * 1024 * 1024
        handler = RotatingFileHandler(self._pwd(), 'a', calc, 10)
        handler.setFormatter(self._formatter())
        return handler

    def _formatter(self):
        return logging.Formatter(self.info_format, self.timestamp_format)

    def _pwd(self):
        return "logs/{file}.log".format(file=self.file)
