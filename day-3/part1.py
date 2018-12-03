#!/usr/bin/env python 
import re

regex = "^(#(?P<ClaimId>[0-9]{0,}) @ (?P<FromLeftEdge>[0-9]{0,}),(?P<FromTopEdge>[0-9]{0,}): (?P<Width>[0-9]{0,4})x(?P<Height>[0-9]{0,4}).*)$"

class Claim(object):
    def __init__(self, line):
        match = re.search(regex, line)
        self.ClaimId = match.group('ClaimId')
        self.FromLeftEdge = int(match.group('FromLeftEdge'))
        self.FromTopEdge  = int(match.group('FromTopEdge'))
        self.Width = int(match.group('Width'))
        self.Height = int(match.group('Height'))

    def __str__(self):
        return "ClaimId: " + str(self.ClaimId) + "\n\tFromLeftEdge: " + str(self.FromLeftEdge) + "\tFromTopEdge: " + str(self.FromTopEdge) +  "\tWidth: " + str(self.Width) + "\tHeight: " + str(self.Height)
    
    def updateCloth(self, cloth):
        for x in range(self.FromLeftEdge, self.FromLeftEdge + self.Width):
            for y in range(self.FromTopEdge, self.FromTopEdge + self.Height):
                cloth[x][y] = cloth[x][y] + 1

def main():
    claims = []
    maxWidth = 0
    maxHeight = 0

    # read in all the claims, and find the max/min's for the heigh and width.
    with open("input.txt") as f:
        for line in f:
            claim = Claim(line)
            claims.append(claim)
            compareWidth = claim.FromLeftEdge + claim.Width
            compareHeight = claim.FromTopEdge + claim.Height
            maxWidth = compareWidth if compareWidth > maxWidth else maxWidth
            maxHeight = compareHeight if compareHeight > maxHeight else maxHeight 
    
    # build up the cloth
    cloth = [0] * maxWidth
    for x in range(maxWidth):
        cloth[x] = [0] * maxHeight
    
    # update the cloth with all the claims
    for claim in claims:
        claim.updateCloth(cloth)
    
    # find the overlapping claims
    overlapCount = 0
    for x in range(len(cloth)):
        for y in range(len(cloth[x])):
            if cloth[x][y] > 1:
                overlapCount = overlapCount + 1  

    print("Overlap Count: " + str(overlapCount))

if __name__ == "__main__":
    main()