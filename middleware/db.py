from peewee import ModelSelect

class Db(object):
    def __init__(self):
        def sort(self, **kwargs):
            return self.order_by(getattr(getattr(self.model, kwargs['column']), kwargs['order'])())

        def iterable(self):
            return list(self)

        setattr(ModelSelect, 'sort', sort)
        setattr(ModelSelect, 'iterable', iterable)
