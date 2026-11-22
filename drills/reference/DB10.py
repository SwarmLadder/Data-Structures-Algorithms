"""DB10 reference: Undo with backspaces. Open after your own attempt."""
def solve(s):
    stack = []
    for ch in s:
        if ch == "#":
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
