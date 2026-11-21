"""Reference answer for I14. See the problem statement before reading.
"""
def solve(tree):
    from collections import deque
    if not tree or tree[0] is None:
        return []
    queue = deque([(0,0)])
    answer = []
    while queue:
        index, depth = queue.popleft()
        if index >= len(tree) or tree[index] is None:
            continue
        if len(answer) == depth:
            answer.append([])
        answer[depth].append(tree[index])
        queue.append((index*2+1, depth+1))
        queue.append((index*2+2, depth+1))
    return answer
