"""Inventory reconciler: your implementation. See README.md for the tickets.

Run: python -m tools.projects check basics/01_inventory_reconciler
"""
def parse(lines):
    """'SKU,qty' lines -> {sku: total qty}. Blank lines and '#' comments are ignored; repeated SKUs add up."""
    raise NotImplementedError('implement parse')

def diff(expected, counted):
    """Sorted list of (sku, expected, counted) for every SKU whose quantities differ (missing = 0)."""
    raise NotImplementedError('implement diff')

def merge_sorted_skus(a, b):
    """Merge two sorted, duplicate-free SKU lists into one sorted, duplicate-free list in O(len(a) + len(b))."""
    raise NotImplementedError('implement merge_sorted_skus')

def worst(discrepancies, k):
    """The k discrepancies with the largest absolute difference; ties by SKU."""
    raise NotImplementedError('implement worst')
