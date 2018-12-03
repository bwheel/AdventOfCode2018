#!/usr/bin/env python

boxId1 = ""
boxId2 = ""
lines = []
with open("input.txt") as f:
    lines = f.readlines()

n = len(lines)

# iterate through the box id's
for i in range(n):
    boxId1 = lines[i]
    testLine = list(boxId1)
    #print("Testing: " + boxId1)
    # iterate through the rest of the box id's
    for j in range(0, n -i -1):
        boxId2 = lines[j]
        compareLine = list(boxId2)
        #print("\tagainst: " + boxId2)
        # calculate the difference by character
        diffCount = 0
        for c in range(len(testLine)):
            if testLine[c] != compareLine[c]:
                diffCount = diffCount + 1
        
        if diffCount == 1:
            break

    if diffCount == 1:
            break

sameLetters = ""
print("Box 1: " + boxId1 + "Box 2: " + boxId2)
for i in range(len(boxId1)):
    if testLine[i] == compareLine[i]:
        sameLetters = sameLetters + testLine[i]
print("Same letters: " + sameLetters)