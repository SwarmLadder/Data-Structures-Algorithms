"""DB48 reference: Which inputs break it?. Open after your own attempt."""
def solve(inputs):
    return [i for i, x in enumerate(inputs) if not x]
