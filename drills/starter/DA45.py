"""DA45 — Critical path length (guided)

tasks maps names to durations; deps is a list of [before, after]. With unlimited
workers, return the time at which all tasks finish (the longest dependency path).
The graph is a DAG.

Check: python -m tools.drills check DA45
Hints: python -m tools.drills hint DA45 1
"""

___ = None  # replace every ___ below with your code

def solve(tasks, deps):
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
        finish[t] = start[t] + ___
        for nxt in after[t]:
            start[nxt] = max(start[nxt], ___)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                ready.append(nxt)
    return max(finish.values(), default=0)
