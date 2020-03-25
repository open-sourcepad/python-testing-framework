for dtype in [
    'int',
    'float',
    'str',
    'list',
    'dict',
    'tuple'
]:
    exec(f"""
def to_{ dtype }(value):

    try:
        return {dtype}(value)
    except Exception as e:
        return value
    """)
