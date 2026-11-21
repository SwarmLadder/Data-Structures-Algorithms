"""Reference answer for I09. See the problem statement before reading.
"""
def solve(latencies):
    result = [0] * len(latencies)
    waiting = []
    for i, value in enumerate(latencies):
        while waiting and latencies[waiting[-1]] < value:
            j = waiting.pop()
            result[j] = i - j
        waiting.append(i)
    return result
