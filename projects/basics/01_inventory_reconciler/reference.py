"""Inventory reconciler: reference implementation. Open after your own attempt."""


def parse(lines):
    """'SKU,qty' lines -> {sku: total qty}. Blank lines and '#' comments are ignored; repeated SKUs add up."""
    totals = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        sku, qty = line.split(",")
        totals[sku.strip()] = totals.get(sku.strip(), 0) + int(qty)
    return totals


def diff(expected, counted):
    """Sorted list of (sku, expected, counted) for every SKU whose quantities differ (missing = 0)."""
    skus = sorted(set(expected) | set(counted))
    return [(s, expected.get(s, 0), counted.get(s, 0)) for s in skus if expected.get(s, 0) != counted.get(s, 0)]


def merge_sorted_skus(a, b):
    """Merge two sorted, duplicate-free SKU lists into one sorted, duplicate-free list in O(len(a) + len(b))."""
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            out.append(a[i]); i += 1; j += 1
        elif a[i] < b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]


def worst(discrepancies, k):
    """The k discrepancies with the largest absolute difference; ties by SKU."""
    return sorted(discrepancies, key=lambda d: (-abs(d[1] - d[2]), d[0]))[:k]
