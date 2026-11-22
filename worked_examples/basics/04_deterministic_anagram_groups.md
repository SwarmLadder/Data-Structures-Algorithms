# Worked example B4 · Anagram groups with a deterministic order

**Problem.** Group words that are anagrams of each other. Each group must be sorted alphabetically, and the groups sorted by their first word. Duplicates are kept.

## 1. Plan

Anagrams share a **canonical key**: their letters in sorted order. A dictionary from key to list builds the groups in one pass; the ordering requirements are applied afterwards, explicitly.

## 2. Tempting attempt

```python
def groups_unordered(words):
    groups = {}
    for w in words:
        groups.setdefault("".join(sorted(w)), []).append(w)
    return list(groups.values())

print(groups_unordered(["tear", "eat", "rate", "tea", "ate"]))
```

<!-- output -->
```text
[['tear', 'rate'], ['eat', 'tea', 'ate']]
```
<!-- /output -->

The grouping is right, but the order follows the input (dict insertion order), not the contract: `"tear"` comes before `"rate"`, and the `eat` group should come first.

## 3. Fix: sort inside, then sort the groups

```python
def anagram_groups(words):
    groups = {}
    for w in words:
        groups.setdefault("".join(sorted(w)), []).append(w)
    return sorted(sorted(g) for g in groups.values())   # lists compare by first word, then the rest

print(anagram_groups(["tear", "eat", "rate", "tea", "ate"]))
print(anagram_groups(["ab", "ba", "ab"]))              # duplicates kept
print(anagram_groups([]))
```

<!-- output -->
```text
[['ate', 'eat', 'tea'], ['rate', 'tear']]
[['ab', 'ab', 'ba']]
[]
```
<!-- /output -->

For a fixed alphabet, a 26-count tuple key avoids sorting each word: O(k) instead of O(k log k) per word.

```python
def count_key(word):
    counts = [0] * 26
    for ch in word:
        counts[ord(ch) - 97] += 1
    return tuple(counts)

print(count_key("tea") == count_key("ate"), count_key("tea") == count_key("tee"))
```

<!-- output -->
```text
True False
```
<!-- /output -->

## 4. Test it

The output must not depend on the input order, which is a **metamorphic** property:

```python
import random
random.seed(4)
pool = ["listen", "silent", "enlist", "google", "gogole", "cat", "act", "tac", "dog"]
expected = anagram_groups(pool)
for _ in range(500):
    shuffled = random.sample(pool, len(pool))
    assert anagram_groups(shuffled) == expected
print("500 shuffles give identical output:", expected[:2], "...")
```

<!-- output -->
```text
500 shuffles give identical output: [['act', 'cat', 'tac'], ['dog']] ...
```
<!-- /output -->

**Practise next:** drills `DB02`, `DB04`; interview problems `B02`, `B09`.
