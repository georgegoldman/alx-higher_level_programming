#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_digit = number % 10 if number >= 0 else ((-number % 10) * -1)
str = f"Last digit of {number} is {last_digit}"
if last_digit == 0:
    last_digit = -last_digit
    print(f"{str} and is 0")
elif last_digit > 5 and last_digit % 10 != 0:
    print(f"{str} and is greater than 5")
else:
    print(f"{str} and is less than 6 and not 0")
