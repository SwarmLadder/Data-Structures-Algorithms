"""Undo/redo text editor: your implementation. See README.md for the tickets.

Run: python -m tools.projects check basics/02_undo_editor
"""
class Editor:
    """A single-line editor with a cursor, typing, deleting, undo and redo."""

    def __init__(self):
        pass

    def _save(self):
        raise NotImplementedError('implement _save')

    def type(self, s):
        """Insert s at the cursor and move the cursor after it."""
        raise NotImplementedError('implement type')

    def backspace(self, n=1):
        """Delete up to n characters before the cursor."""
        raise NotImplementedError('implement backspace')

    def move(self, k):
        """Move the cursor by k (negative = left), clamped to the text. Moving is not undoable."""
        raise NotImplementedError('implement move')

    def undo(self):
        """Revert the most recent change; return False if there is nothing to undo."""
        raise NotImplementedError('implement undo')

    def redo(self):
        """Re-apply the most recently undone change; return False if there is nothing to redo."""
        raise NotImplementedError('implement redo')
