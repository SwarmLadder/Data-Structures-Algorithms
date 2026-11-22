"""DB35 reference: Sliding-window maximum. Open after your own attempt."""
from collections import deque

def solve(values, k):
    dq, out = deque(), []
    for i, v in enumerate(values):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and values[dq[-1]] <= v:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(values[dq[0]])
    return out
