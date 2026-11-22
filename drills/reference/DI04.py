"""DI04 reference: Is a permutation of p inside s?. Open after your own attempt."""
def solve(p, s):
    from collections import Counter
    k = len(p)
    if k == 0:
        return True
    need, window = Counter(p), Counter(s[:k])
    if window == need:
        return True
    for i in range(k, len(s)):
        window[s[i]] += 1
        window[s[i - k]] -= 1
        if window[s[i - k]] == 0:
            del window[s[i - k]]
        if window == need:
            return True
    return False
