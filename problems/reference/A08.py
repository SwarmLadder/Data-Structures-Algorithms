"""Reference answer for A08. See the problem statement before reading.
"""
def solve(text, dictionary):
    words = set(dictionary)
    lengths = {len(w) for w in words}
    dp = [False] * (len(text) + 1)
    dp[0] = True
    for end in range(1,len(text)+1):
        dp[end] = any(end >= length and dp[end-length] and text[end-length:end] in words for length in lengths)
    return dp[-1]
