#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ptr = str(number)
num = int(ptr[-1])
if num > 5 and number >= 0:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0 and number >= 0:
    print(f"Last digit of {number} is 0 and is 0")
elif num > 0 and num <= 5 and number >= 0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
elif number < 0 and num <= 5:
    if num == 0:
	print(f"Last digit of {number} is 0 and is 0")
elif
    print(f"Last digit of {number} is {-1 * num} and is less than 6 and not 0")
