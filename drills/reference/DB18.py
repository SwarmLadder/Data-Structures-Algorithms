"""DB18 reference: How many halvings?. Open after your own attempt."""
def solve(n):
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps
