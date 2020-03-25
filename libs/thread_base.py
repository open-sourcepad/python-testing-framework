from .logger import Logger

from threading import Thread

class ThreadBase:
    def __init__(self, **kwargs):
        self.thread = Thread(target=self.perform, kwargs=kwargs)

    def run(self):
        try:
            self.thread.start()
        except Exception as e:
            self.log_error(message=str(e.__class__))

    def log_info(self, **kwargs):
        kwargs.update({'type': 'info'})
        self._logger(**kwargs)

    def log_error(self, **kwargs):
        message = "Error occurred {error}".format(error=kwargs['message'])
        kwargs.update({
            'type': 'error',
            'message': message
        })
        self._logger(**kwargs)

    def _logger(self, **kwargs):
        Logger(
            message=kwargs['message'],
            file=kwargs.get('file', 'thread_error'),
            type=kwargs['type']
        ).log()
