"""DB20 — Classify a growth rate (independent)

steps[i] is the measured work at input size sizes[i] (sizes double each time).
Return 'constant', 'linear' or 'quadratic' depending on whether the work stays the
same, roughly doubles, or roughly quadruples between the last two measurements (use
the ratio: < 1.5, < 3, otherwise).

Check: python -m tools.drills check DB20
Hints: python -m tools.drills hint DB20 1
"""

def solve(sizes, steps):
    raise NotImplementedError("Implement solve")
