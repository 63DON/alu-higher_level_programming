#!/usr/bin/python3
"""Define a function that checks for a lowercase character."""

def islower(c):
    """Return True if c is lowercase, False otherwise."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
