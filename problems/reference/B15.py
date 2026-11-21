"""Reference answer for B15. See the problem statement before reading.
"""
def solve(paths):
    if not paths:
        return ''
    prefix = paths[0]
    for path in paths[1:]:
        while not path.startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            return ''
    return prefix
