"""Reference answer for A15. See the problem statement before reading.
"""
def solve(sizes, target):
    values = sorted(sizes)
    result = []
    def dfs(start, remaining, path):
        if remaining == 0:
            result.append(path[:]); return
        for i in range(start,len(values)):
            size = values[i]
            if size > remaining: break
            path.append(size)
            dfs(i,remaining-size,path)
            path.pop()
    dfs(0,target,[])
    return result
