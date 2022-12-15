#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_digit = abs(number) % 10
if last_digit == 0:
    last_digit = -last_digit
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
elif last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
