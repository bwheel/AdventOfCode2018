#!/usr/bin/env python

sum = 0
with open("input.txt") as f:
    for line in f:
        sum = sum + int(line)
print("Sum: " + str(sum))