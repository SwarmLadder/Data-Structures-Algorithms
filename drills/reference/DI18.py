"""DI18 reference: Stock span. Open after your own attempt."""
def solve(prices):
    stack, out = [], []
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] <= p:
            stack.pop()
        out.append(i - stack[-1] if stack else i + 1)
        stack.append(i)
    return out
