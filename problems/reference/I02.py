"""Reference answer for I02. See the problem statement before reading.
"""
def solve(text, required):
    from collections import Counter
    if not required:
        return ''
    need = Counter(required)
    missing = len(required)
    left = 0
    best = (len(text) + 1, -1, -1)
    for right, char in enumerate(text):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            need[text[left]] += 1
            if need[text[left]] > 0:
                missing += 1
            left += 1
    return text[best[1]:best[2]] if best[1] >= 0 else ''
