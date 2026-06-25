#!/usr/bin/python3
"""Define a function that prints the last digit of a number."""


def print_last_digit(number):
    """Print the last digit of a number and return its value."""
    last_digit = number % 10
    if number < 0 and last_digit != 0:
        last_digit -= 10
    print(last_digit, end="")
    return last_digit
