"""DI11 reference: LRU cache simulator. Open after your own attempt."""
from collections import OrderedDict

def solve(capacity, ops):
    data, out = OrderedDict(), []
    for op in ops:
        if op[0] == "get":
            key = op[1]
            if key in data:
                data.move_to_end(key)
                out.append(data[key])
            else:
                out.append(-1)
        else:
            _, key, value = op
            data[key] = value
            data.move_to_end(key)
            if len(data) > capacity:
                data.popitem(last=False)
    return out
