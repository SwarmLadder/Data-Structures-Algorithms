"""Reference answer for A10. See the problem statement before reading.
"""
def solve(source, target):
    previous = list(range(len(target)+1))
    for i,a in enumerate(source,1):
        current = [i] + [0]*len(target)
        for j,b in enumerate(target,1):
            current[j] = min(previous[j]+1,current[j-1]+1,previous[j-1]+(a!=b))
        previous = current
    return previous[-1]
