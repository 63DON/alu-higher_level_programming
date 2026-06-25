#!/usr/bin/python3
"""Print whether a randomly generated number is positive, negative, or zero."""
import random

number = random.randint(-10, 10)

if number > 0:
      print("{} is positive".format(number))
elif number == 0:
      print("{} is zero".format(number))
else:
      print("{} is negative".format(number))
  
