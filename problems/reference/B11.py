"""Reference answer for B11. See the problem statement before reading.
"""
def solve(source, masked):
    if len(source) != len(masked):
        return False
    forward, backward = {}, {}
    for a, b in zip(source, masked):
        if a in forward and forward[a] != b:
            return False
        if b in backward and backward[b] != a:
            return False
        forward[a] = b
        backward[b] = a
    return True
