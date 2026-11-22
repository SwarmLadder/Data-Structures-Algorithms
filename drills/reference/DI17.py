"""DI17 reference: Next greater element. Open after your own attempt."""
def solve(values):
    answer, stack = [-1] * len(values), []
    for i, v in enumerate(values):
        while stack and values[stack[-1]] < v:
            answer[stack.pop()] = v
        stack.append(i)
    return answer
