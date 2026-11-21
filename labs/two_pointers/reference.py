"""Reference implementation — read after attempting starter.py."""

def move_zeros(values: list[int]) -> None:
    """Compact nonzero values, then zero the unused suffix in place."""
    write = 0
    for read in range(len(values)):
        if values[read] != 0:
            values[write] = values[read]
            write += 1
    for i in range(write, len(values)):
        values[i] = 0
