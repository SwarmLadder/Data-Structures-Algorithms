"""DA41 reference: A tiny differential tester. Open after your own attempt."""
def solve(inputs):
    def oracle(x):
        return sorted(x)
    def candidate(x):
        return list(x) if len(x) == 2 else sorted(x)
    return [x for x in inputs if candidate(x) != oracle(x)]
