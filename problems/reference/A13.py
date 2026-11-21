"""Reference answer for A13. See the problem statement before reading.
"""
def solve(words, prefix, k):
    root = {}
    for word in set(words):
        node = root
        for ch in word:
            node = node.setdefault(ch,{})
        node['#'] = True
    node = root
    for ch in prefix:
        if ch not in node: return []
        node = node[ch]
    if k == 0: return []
    result = []
    stack = [(node,prefix)]
    while stack and len(result) < k:
        current,path = stack.pop()
        if '#' in current:
            result.append(path)
        for ch in sorted((c for c in current if c != '#'),reverse=True):
            stack.append((current[ch],path+ch))
    return result
