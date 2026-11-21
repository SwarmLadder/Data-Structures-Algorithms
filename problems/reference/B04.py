"""Reference answer for B04. See the problem statement before reading.
"""
def solve(text):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in text:
        if ch in '([{':
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack
