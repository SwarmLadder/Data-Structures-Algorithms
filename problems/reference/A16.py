"""Reference answer for A16. See the problem statement before reading.
"""
def solve(a, b):
    if len(a) > len(b):
        a,b = b,a
    m,n = len(a),len(b)
    lo,hi = 0,m
    half = (m+n+1)//2
    while lo <= hi:
        i = (lo+hi)//2
        j = half-i
        al = a[i-1] if i else float('-inf')
        ar = a[i] if i<m else float('inf')
        bl = b[j-1] if j else float('-inf')
        br = b[j] if j<n else float('inf')
        if al <= br and bl <= ar:
            if (m+n)%2:
                return float(max(al,bl))
            return (max(al,bl)+min(ar,br))/2.0
        if al > br: hi = i-1
        else: lo = i+1
    raise ValueError('Arrays must be sorted')
