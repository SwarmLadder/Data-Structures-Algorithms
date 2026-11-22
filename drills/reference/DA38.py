"""DA38 reference: Amortised cost of doubling. Open after your own attempt."""
def solve(n):
    capacity, size, copies = 1, 0, 0
    for _ in range(n):
        if size == capacity:
            copies += size
            capacity *= 2
        size += 1
    return copies
