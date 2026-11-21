"""Reference answer for I16. See the problem statement before reading.
"""
def solve(next_index, start):
    def step(i):
        return -1 if i == -1 else next_index[i]
    slow = fast = start
    while fast != -1 and step(fast) != -1:
        slow = step(slow)
        fast = step(step(fast))
        if slow == fast:
            return True
    return False
