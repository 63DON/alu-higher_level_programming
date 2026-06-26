#!/usr/bin/python3
"""Import calculator functions and print the results"""
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    r1 = add(a, b)
    r2 = sub(a, b)
    r3 = mul(a, b)
    r4 = div(a, b)
    print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(
        a, b, r1, a, b, r2, a, b, r3, a, b, r4))
