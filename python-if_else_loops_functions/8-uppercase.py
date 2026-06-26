#!/usr/bin/python3
"""Define a function that prints a string in uppercase."""


def uppercase(str):
    """Print a string in uppercase, followed by a new line."""
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            result += "{:c}".format(ord(c) - 32)
        else:
            result += "{:c}".format(ord(c))
    print("{}".format(result))
