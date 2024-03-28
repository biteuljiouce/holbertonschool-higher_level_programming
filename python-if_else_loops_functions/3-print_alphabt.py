#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    endChar = ""
#    if i == 122:
#        endChar = "\n"
    print("{}".format(chr(i)), end=endChar)
