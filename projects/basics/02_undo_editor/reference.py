"""Undo/redo text editor: reference implementation. Open after your own attempt."""


class Editor:
    """A single-line editor with a cursor, typing, deleting, undo and redo."""

    def __init__(self):
        self.text = ""
        self.cursor = 0
        self._undo = []          # stack of (text, cursor) snapshots before each change
        self._redo = []

    def _save(self):
        self._undo.append((self.text, self.cursor))
        self._redo.clear()       # a new change invalidates the redo history

    def type(self, s):
        """Insert s at the cursor and move the cursor after it."""
        if not s:
            return
        self._save()
        self.text = self.text[:self.cursor] + s + self.text[self.cursor:]
        self.cursor += len(s)

    def backspace(self, n=1):
        """Delete up to n characters before the cursor."""
        n = min(n, self.cursor)
        if n == 0:
            return
        self._save()
        self.text = self.text[:self.cursor - n] + self.text[self.cursor:]
        self.cursor -= n

    def move(self, k):
        """Move the cursor by k (negative = left), clamped to the text. Moving is not undoable."""
        self.cursor = max(0, min(len(self.text), self.cursor + k))

    def undo(self):
        """Revert the most recent change; return False if there is nothing to undo."""
        if not self._undo:
            return False
        self._redo.append((self.text, self.cursor))
        self.text, self.cursor = self._undo.pop()
        return True

    def redo(self):
        """Re-apply the most recently undone change; return False if there is nothing to redo."""
        if not self._redo:
            return False
        self._undo.append((self.text, self.cursor))
        self.text, self.cursor = self._redo.pop()
        return True
