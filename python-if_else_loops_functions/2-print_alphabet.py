#!/usr/bin/python3
"""Print the lowercase ASCII alphabet, without a trailing new line."""
for i in range(97, 123):
    print("{:c}".format(i), end="")
