#!/usr/bin/env python

history = {}
currentFreq = 0
duplicateFrequency = 0

discoveredDuplicate = False
# debug variables
rowCount = 0

with open("input.txt") as f:
    while not discoveredDuplicate :
        for line in f:
            rowCount = rowCount + 1
            change = int(line)
            currentFreq = currentFreq + change
            #print("New frequency: " + str(currentFreq))
            #print("history size: " + str(len(history)))
            if history.has_key(currentFreq):
                duplicateFrequency = currentFreq
                discoveredDuplicate = True
                break
            else:
                history[currentFreq] = 0
        f.seek(0)

print("Row Count: " + str(rowCount))
print("Duplicate Frequency: " + str(duplicateFrequency))
