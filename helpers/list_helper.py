def pluck(**kwargs):
    values = kwargs['values']
    key = kwargs['key']

    if type(values) == dict:
        result = [value[key] for value in values]
    else:
        result = [getattr(value, key) for value in values]

    return result

def compact(list_data):
    return [x for x in list_data if x is not None]

def uniq(list_data):
    return list(set(list_data))
