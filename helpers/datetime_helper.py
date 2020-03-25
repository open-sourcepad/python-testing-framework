from datetime import datetime as DT

def str_to_date(value, format='%Y-%m-%d %H:%M:%S.%f'):
    return DT.strptime(value, format)

def get_beginning_of_week(**kwargs):
    day = kwargs['datetime']
    if type(kwargs['datetime']) == str:
        day = convert_to_datetime(kwargs['datetime'])
    result = day - timedelta(days=day.weekday())

    return result

def get_end_of_week(**kwargs):
    day = kwargs['datetime']
    if type(kwargs['datetime']) == str:
        day = convert_to_datetime(kwargs['datetime'])
    result = day + timedelta(days=(6 - day.weekday()))

    return result
