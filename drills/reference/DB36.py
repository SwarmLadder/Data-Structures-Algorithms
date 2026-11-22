"""DB36 reference: Recent calls counter. Open after your own attempt."""
from collections import deque

def solve(times):
    window, out = deque(), []
    for t in times:
        window.append(t)
        while window[0] < t - 3000:
            window.popleft()
        out.append(len(window))
    return out
