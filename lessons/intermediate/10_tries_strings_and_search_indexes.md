# Tries and string algorithms: how to index prefixes

**Outcome:** understand prefix trees, lexicographic output and when a simpler sorted index is better. **Time:** 90 minutes.

## 1. Choose the string query

A **prefix search** asks for keys beginning with a given prefix. A **substring search** asks whether a pattern occurs anywhere in a text. These are different problems: a trie helps prefix lookup; it is not automatically an optimal substring search algorithm.

A trie node stores edges labeled by characters and a terminal marker for complete words. Searching or inserting a word of length L takes O(L) character operations, assuming constant-time child lookup. Total storage is bounded by total characters inserted, although real Python dictionaries per node have substantial overhead.

## 2. Minimal trie implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.terminal = True

    def contains(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.terminal
```

Note: Python eagerly constructs the default argument in `setdefault(ch, TrieNode())`, even if ch already exists. That makes an unnecessary node allocation per character. Optimize with an explicit membership check or `defaultdict(TrieNode)` when allocation matters.

## 3. Lexicographic suggestions

To suggest up to k commands matching prefix p, traverse the trie to the node after p. Then DFS through child keys in sorted order; whenever a terminal node is reached, emit the word. Stop after k outputs. If duplicates in the input are not supposed to appear twice, a boolean terminal marker naturally deduplicates them. Complexity includes prefix length plus the number of traversed trie nodes; do **not** claim universal O(|p|+k) when exploring long paths or nonmatching branches.

For static data with moderate size, a sorted list plus binary search on the first prefix match may be simpler. Prefix query costs O(log n + candidates scanned × string work); it avoids many node objects. Choose based on memory, update frequency and the exact requested result order.

## 4. String matching alternatives

Naive substring search compares the pattern at every start position: O(nm) worst-case for text length n and pattern length m. KMP preprocesses a prefix-function/failure table and scans in O(n+m). Rolling hashes can support expected fast comparison but require collision verification for exact correctness. Do not describe hashing as collision-free without strong assumptions.

## 5. Edge cases and exercises

- Empty prefix matches every word; empty word is a valid terminal at the root.
- Inputs may have duplicate words; decide whether suggestions are unique.
- k=0 must return an empty list without exploring the subtree.
- Lexicographic order is not insertion order; sort child labels or maintain another ordering structure.
- Design a trie for Unicode or case-insensitive words only after defining normalization semantics.

**Practice:** A13. Add insert/search/prefix methods and compare memory/performance with `sorted(set(words))` plus `bisect`. **Mastery checkpoint:** Explain the path-length complexity, what a terminal means, and why trie traversal and substring search solve different problems.
