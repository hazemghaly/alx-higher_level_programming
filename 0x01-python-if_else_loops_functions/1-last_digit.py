#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ptr = str(number)
num = int(ptr[-1])
if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif num > 0 and num <= 5:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
