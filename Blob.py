import os
import sqlite3

class Blob:
    """Automatically encode a binary string."""
    def __init__(self, s):
        self.s = s

    def _quote(self):
        return "'%s'" % sqlite3.encode(self.s)
