

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 34:
        return 34
    else:
        return


def new_string(symbol, count):
    return symbol * count


def con(*params):
    res: str = ""
    for item in params:
        res += item
    return res

