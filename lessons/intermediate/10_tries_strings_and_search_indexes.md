# Tries and string algorithms: how to index prefixes

**Outcome:** understand prefix trees, lexicographic output and when a simpler sorted index is better. **Time:** 90 minutes.

**Study time:** 90–120 minutes · **Before this:** [Greedy algorithms: prove the local choice is globally safe](09_greedy_algorithms_and_exchange_arguments.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
class PrefixTrie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True                     # end-of-word marker
    def has_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
    def words_with(self, prefix):
        node = self.root
        for ch in prefix:
            node = node.get(ch)
            if node is None:
                return []
        out = []
        def dfs(n, path):
            if "$" in n:
                out.append(prefix + path)
            for ch in sorted(k for k in n if k != "$"):
                dfs(n[ch], path + ch)
        dfs(node, "")
        return out

t = PrefixTrie()
for w in ["deploy", "delete", "describe", "diff", "de"]:
    t.insert(w)
print(t.has_prefix("dep"), t.has_prefix("dx"))
print(t.words_with("de"))
```

<!-- output -->
```text
True False
['de', 'delete', 'deploy', 'describe']
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| No end-of-word marker | 'de' looks present after inserting 'deploy' | Mark word ends explicitly |
| Sorting children inconsistently | Suggestions in random order | Visit children in sorted order |
| Building a trie for a single lookup | Overkill: O(total length) setup | A set or sorting may be enough |
| Forgetting the empty prefix | Missing 'all words' case | The root represents the empty prefix |
| Storing whole words at every node | Memory blow-up | Store characters per edge; reconstruct paths |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI37` | **Longest common prefix.** Return the longest common prefix of all strings in words ('' for an empty list). | guided |
| `DI38` | **Trie: which queries are prefixes?.** Insert every word into a trie (nested dicts), then return a list of booleans: for each query, whether some word starts with it. | guided |
| `DI39` | **Autocomplete top three.** For each prefix of query (query[:1], query[:2], …), return up to three words from words that start with it, in lexicographic order. | independent |
| `DI40` | **Replace words with roots.** Replace every word in sentence with the shortest root from roots that is a prefix of it (keep the word if none). Return the new sentence. | independent |

```bash
python -m tools.drills show DI37
python -m tools.drills check DI37
python -m tools.drills hint DI37 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A13`, `B15`. Read one with `python -m tools.practice show A13 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Looking up a word of length L in a trie costs…

   - **a)** O(L)
   - **b)** O(number of words)
   - **c)** O(log n)

**2.** Why does a trie need an end-of-word marker?

   - **a)** To save memory
   - **b)** So a stored prefix like 'de' is distinguishable from a word
   - **c)** For sorting

**3.** How do you return suggestions in lexicographic order from a trie?

   - **a)** DFS visiting children in sorted order
   - **b)** BFS
   - **c)** Random order then sort

**4.** When is a sorted list with binary search a good alternative to a trie?

   - **a)** Never
   - **b)** When the word list is static and prefix queries are moderate
   - **c)** Only for numbers

```bash
python -m tools.quiz intermediate/10 1 b      # question 1, answer b
python -m tools.quiz intermediate/10           # list the questions
```
<!-- /quiz -->

## Summary

- A trie stores strings by shared prefixes; lookups cost O(length), independent of word count.
- Mark word ends: a prefix is not necessarily a word.
- DFS in sorted child order yields lexicographic suggestions.
- Choose tries for many prefix queries; sets or sorted lists for simpler needs.

**Next:** [Backtracking: enumerate candidates without corrupting state](11_backtracking_pruning_and_state_restoration.md)
