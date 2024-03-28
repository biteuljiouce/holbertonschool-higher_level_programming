#!/usr/bin/python3
lastIndex = 100
for i in range(lastIndex):
    endChar = ", "
    if (i == lastIndex - 1):
        endChar = "\n"
    print("{0:02d}".format(i), end=endChar)
