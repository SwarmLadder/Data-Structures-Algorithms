"""DB20 reference: Classify a growth rate. Open after your own attempt."""
def solve(sizes, steps):
    ratio = steps[-1] / steps[-2]
    if ratio < 1.5:
        return "constant"
    if ratio < 3:
        return "linear"
    return "quadratic"
