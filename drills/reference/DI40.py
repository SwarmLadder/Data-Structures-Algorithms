"""DI40 reference: Replace words with roots. Open after your own attempt."""
def solve(roots, sentence):
    trie = {}
    for r in roots:
        node = trie
        for ch in r:
            node = node.setdefault(ch, {})
        node["$"] = True
    out = []
    for word in sentence.split():
        node, replaced = trie, word
        for i, ch in enumerate(word):
            if ch not in node:
                break
            node = node[ch]
            if "$" in node:
                replaced = word[:i + 1]
                break
        out.append(replaced)
    return " ".join(out)
