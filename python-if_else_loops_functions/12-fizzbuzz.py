#!/usr/bin/python3
"""Define a function that prints numbers 1 to 100 as FizzBuzz."""


def fizzbuzz():
    """Print the numbers from 1 to 100, applying FizzBuzz rules."""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
