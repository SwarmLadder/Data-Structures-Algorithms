"""Autocomplete service: your implementation. See README.md for the tickets.

Run: python -m tools.projects check intermediate/02_autocomplete_service
"""
import heapq

class Autocomplete:
    """Suggest the k most frequent completions of a prefix; ties broken alphabetically."""

    def __init__(self, k=3):
        pass

    def record(self, query, times=1):
        """Count `times` more searches for `query`."""
        raise NotImplementedError('implement record')

    def suggest(self, prefix):
        """Up to k completions of prefix ordered by (-count, query)."""
        raise NotImplementedError('implement suggest')

    def top_overall(self, k):
        """The k most searched queries overall."""
        raise NotImplementedError('implement top_overall')
