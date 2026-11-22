"""DI19 reference: Largest rectangle in a histogram. Open after your own attempt."""
def solve(heights):
    stack, best = [], 0
    hs = heights + [0]
    for i, h in enumerate(hs):
        while stack and hs[stack[-1]] >= h:
            height = hs[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best
