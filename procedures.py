from importlib import import_module

class Procedures:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.test = kwargs.get('test')

    def run(self):
        if self.test:
            return self._run(self.test)

    def run_all(self):
        result = []
        for module in self._module_list:
            result.append(self._run(module))

        return result

    @property
    def _module_list(self):
        return [
            'sample'
        ]

    def _run(self, module_name):
        package = ''.join([split.capitalize() for split in module_name.split('_')])
        module = import_module(f"modules.{module_name}")
        return getattr(module, package)(**self.kwargs).run()
