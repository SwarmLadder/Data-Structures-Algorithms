"""DI18 — Stock span (guided)

For each day, return the span: the number of consecutive days ending today
(including today) with price <= today's price.

Check: python -m tools.drills check DI18
Hints: python -m tools.drills hint DI18 1
"""

___ = None  # replace every ___ below with your code

def solve(prices):
    stack, out = [], []
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] <= p:
            stack.pop()
        out.append(i - stack[-1] if stack else ___)
        stack.append(___)
    return out
