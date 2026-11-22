"""DI38 reference: Trie: which queries are prefixes?. Open after your own attempt."""
def solve(words, queries):
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
    out = []
    for q in queries:
        node = root
        ok = True
        for ch in q:
            if ch not in node:
                ok = False
                break
            node = node[ch]
        out.append(ok)
    return out
