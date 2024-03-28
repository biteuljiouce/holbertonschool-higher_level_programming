#!/usr/bin/python3
rangeLimit = 10
for i in range(rangeLimit):
    for j in range(i + 1, rangeLimit):
        print("{:d}{:d}".format(i, j), end="")
        if (i < rangeLimit - 2):
            print("", end=", ")
        else:
            print("\n", end="")
