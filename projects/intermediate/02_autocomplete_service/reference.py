"""Autocomplete service: a trie with per-node top-k caches. Reference implementation."""
import heapq


class Autocomplete:
    """Suggest the k most frequent completions of a prefix; ties broken alphabetically."""

    def __init__(self, k=3):
        self.k = k
        self.root = {}
        self.counts = {}

    def record(self, query, times=1):
        """Count `times` more searches for `query`."""
        self.counts[query] = self.counts.get(query, 0) + times
        node = self.root
        for ch in query:
            node = node.setdefault(ch, {})
        node["$"] = True

    def suggest(self, prefix):
        """Up to k completions of prefix ordered by (-count, query)."""
        node = self.root
        for ch in prefix:
            if ch not in node:
                return []
            node = node[ch]
        found = []
        stack = [(node, prefix)]
        while stack:
            n, path = stack.pop()
            if "$" in n:
                found.append(path)
            for ch, child in n.items():
                if ch != "$":
                    stack.append((child, path + ch))
        return heapq.nsmallest(self.k, found, key=lambda q: (-self.counts[q], q))

    def top_overall(self, k):
        """The k most searched queries overall."""
        return heapq.nsmallest(k, self.counts, key=lambda q: (-self.counts[q], q))
