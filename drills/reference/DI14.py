"""DI14 reference: Values by level. Open after your own attempt."""
def solve(tree):
    out, level = [], [tree] if tree else []
    while level:
        out.append([node[0] for node in level])
        level = [child for node in level for child in (node[1], node[2]) if child]
    return out
