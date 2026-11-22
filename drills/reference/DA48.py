"""DA48 reference: Deadline check. Open after your own attempt."""
def solve(tasks, deps, deadline):
    after = {t: [] for t in tasks}
    indegree = {t: 0 for t in tasks}
    for a, b in deps:
        after[a].append(b)
        indegree[b] += 1
    start = {t: 0 for t in tasks}
    ready = [t for t in tasks if indegree[t] == 0]
    finish = {}
    while ready:
        t = ready.pop()
        finish[t] = start[t] + tasks[t]
        for nxt in after[t]:
            start[nxt] = max(start[nxt], finish[t])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                ready.append(nxt)
    return sorted(t for t, f in finish.items() if f > deadline)
