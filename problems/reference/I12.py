"""Reference answer for I12. See the problem statement before reading.
"""
def solve(capacity, operations):
    from collections import OrderedDict
    cache = OrderedDict()
    result = []
    for op in operations:
        if op[0] == 'get':
            key = op[1]
            if key not in cache:
                result.append(-1)
            else:
                result.append(cache[key])
                cache.move_to_end(key)
        else:
            key, value = op[1:]
            if key in cache:
                cache.move_to_end(key)
            cache[key] = value
            if len(cache) > capacity:
                cache.popitem(last=False)
    return result
