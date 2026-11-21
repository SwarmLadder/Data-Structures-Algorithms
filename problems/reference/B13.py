"""Reference answer for B13. See the problem statement before reading.
"""
def solve(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i]); i += 1; j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result
