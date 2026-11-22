"""DI34 reference: Assign cookies. Open after your own attempt."""
def solve(greed, sizes):
    greed, sizes = sorted(greed), sorted(sizes)
    child = 0
    for cookie in sizes:
        if child < len(greed) and cookie >= greed[child]:
            child += 1
    return child
