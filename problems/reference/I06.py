"""Reference answer for I06. See the problem statement before reading.
"""
def solve(intervals, new_interval):
    result = []
    a,b = new_interval
    i=0
    while i<len(intervals) and intervals[i][1] < a:
        result.append(intervals[i][:]); i+=1
    while i<len(intervals) and intervals[i][0] <= b:
        a=min(a, intervals[i][0]); b=max(b, intervals[i][1]); i+=1
    result.append([a,b])
    result.extend([v[:] for v in intervals[i:]])
    return result
