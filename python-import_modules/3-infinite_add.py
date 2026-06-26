#!/usr/bin/python3
"""Print the sum of all integer arguments, or 0 if no arguments"""
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{:d}".format(total))
