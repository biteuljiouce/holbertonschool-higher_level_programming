#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if not type(number) is int:
    raise TypeError()
lastDigit = int(str(number)[-1])
if number < 0:
    lastDigit = lastDigit * -1
print("Last digit of {:n} is {:n} ".format(number, int(lastDigit)), end="")
if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
elif lastDigit < 6:
    print("and is less than 6 and not 0")
