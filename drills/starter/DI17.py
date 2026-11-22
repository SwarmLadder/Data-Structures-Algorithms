"""DI17 — Next greater element (guided)

For each value, return the next value to its right that is strictly greater, or -1.

Check: python -m tools.drills check DI17
Hints: python -m tools.drills hint DI17 1
"""

___ = None  # replace every ___ below with your code

def solve(values):
    answer, stack = [-1] * len(values), []
    for i, v in enumerate(values):
        while stack and values[stack[-1]] < v:
            answer[___] = v
        stack.append(___)
    return answer
