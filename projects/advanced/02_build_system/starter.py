"""A tiny build system: your implementation. See README.md for the tickets.

Run: python -m tools.projects check advanced/02_build_system
"""
import heapq

class BuildGraph:

    def __init__(self):
        pass

    def add(self, target, seconds, depends_on=()):
        raise NotImplementedError('implement add')

    def order(self):
        """A build order (dependencies first, ties alphabetical), or raise ValueError naming a cycle member."""
        raise NotImplementedError('implement order')

    def critical_path(self):
        """(total seconds, targets on one longest chain) with unlimited parallelism."""
        raise NotImplementedError('implement critical_path')

    def to_rebuild(self, changed):
        """Every target that must be rebuilt when `changed` targets change (they and all their users), in build order."""
        raise NotImplementedError('implement to_rebuild')
