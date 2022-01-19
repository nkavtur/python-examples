# way1
def pluck1(data: dict, path: str):
    pos = path.find('.')
    if pos == -1:
        return data[path]

    step, next_path = path[:pos], path[pos + 1:]
    return pluck1(data[step], next_path)


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck1(data, 'amount'))
print(pluck1(data, 'category.group'))


# way2
def pluck2(data: dict, path: str):
    split = path.split('.', 1)
    if len(split) == 1:
        return data[path]

    return pluck2(data[split[0]], split[1])


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck2(data, 'amount'))
print(pluck2(data, 'category.group'))


# way3:
def pluck3(data: dict, path: str):
    if '.' not in path:
        return data[path]

    first, *remaining = path.split('.', 1)
    return pluck3(data[first], remaining[0])


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck3(data, 'amount'))
print(pluck3(data, 'category.group'))


# way4:
def pluck4(obj, key_path):
    """Deep-query a dictionary"""
    for key in key_path.split('.'):
        obj = obj[key]
    return obj


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck4(data, 'amount'))
print(pluck4(data, 'category.group'))


# bonus 1
def pluck5(data: dict, path: str, sep='.'):
    first, *remaining = path.split(sep, 1)
    if not remaining:
        return data[first]

    return pluck5(data[first], remaining[0])


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck5(data, 'category/name', sep='/'))


# bonus 2, way1
def pluck6(data: dict, path: str, sep='.', **kwargs):
    try:
        first, *remaining = path.split(sep, 1)
        if not remaining:
            return data[first]

        return pluck7(data[first], remaining[0])
    except KeyError:
        if 'default' in kwargs:
            return kwargs['default']
        else:
            raise


# bonus 2, way2
SENTINEL = object()


def pluck7(data: dict, path: str, sep='.', default=SENTINEL):
    try:
        first, *remaining = path.split(sep, 1)
        if not remaining:
            return data[first]

        return pluck7(data[first], remaining[0])
    except KeyError:
        if default == SENTINEL:
            raise
        return default


# bonus 3
SENTINEL = object()


def pluck(data, *pathes, sep='.', default=SENTINEL):
    def pluck_internally(data, path, sep='.', default=SENTINEL):
        try:
            first, *remaining = path.split(sep, 1)
            if not remaining:
                return data[first]

            return pluck_internally(data[first], remaining[0])
        except KeyError:
            if default == SENTINEL:
                raise
            return default

    res = tuple([
        pluck_internally(data, path, sep, default)
        for path in pathes
    ])

    return res[0] if len(res) == 1 else res


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck(data, 'category.name', 'amount'))
