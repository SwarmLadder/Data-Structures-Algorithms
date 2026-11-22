"""A tiny build system: order targets, find cycles, critical path, and what to rebuild. Reference."""
import heapq


class BuildGraph:
    def __init__(self):
        self.deps = {}          # target -> set of targets it depends on
        self.cost = {}

    def add(self, target, seconds, depends_on=()):
        self.cost[target] = seconds
        self.deps.setdefault(target, set()).update(depends_on)
        for d in depends_on:
            self.deps.setdefault(d, set())
            self.cost.setdefault(d, 0)

    def order(self):
        """A build order (dependencies first, ties alphabetical), or raise ValueError naming a cycle member."""
        users = {t: [] for t in self.deps}
        indegree = {t: len(ds) for t, ds in self.deps.items()}
        for t, ds in self.deps.items():
            for d in ds:
                users[d].append(t)
        ready = [t for t, n in indegree.items() if n == 0]
        heapq.heapify(ready)
        out = []
        while ready:
            t = heapq.heappop(ready)
            out.append(t)
            for u in users[t]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    heapq.heappush(ready, u)
        if len(out) != len(self.deps):
            stuck = min(t for t in self.deps if t not in out)
            raise ValueError(f"dependency cycle involving {stuck}")
        return out

    def critical_path(self):
        """(total seconds, targets on one longest chain) with unlimited parallelism."""
        finish, via = {}, {}
        for t in self.order():
            start, prev = 0, None
            for d in sorted(self.deps[t]):
                if finish[d] > start:
                    start, prev = finish[d], d
            finish[t] = start + self.cost[t]
            via[t] = prev
        if not finish:
            return 0, []
        end = max(sorted(finish), key=lambda t: finish[t])
        chain = []
        while end is not None:
            chain.append(end)
            end = via[end]
        return finish[chain[0]], chain[::-1]

    def to_rebuild(self, changed):
        """Every target that must be rebuilt when `changed` targets change (they and all their users), in build order."""
        users = {t: [] for t in self.deps}
        for t, ds in self.deps.items():
            for d in ds:
                users[d].append(t)
        dirty, stack = set(changed), list(changed)
        while stack:
            for u in users[stack.pop()]:
                if u not in dirty:
                    dirty.add(u)
                    stack.append(u)
        return [t for t in self.order() if t in dirty]
