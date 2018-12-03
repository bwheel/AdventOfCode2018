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
        return "ClaimId: " + str(self.ClaimId) + "\tFromLeftEdge: " + str(self.FromLeftEdge) + "\tFromTopEdge: " + str(self.FromTopEdge) +  "\tWidth: " + str(self.Width) + "\tHeight: " + str(self.Height)
    
class Cloth(object):
    def __init__(self, minHeight, minWidth, maxHeight, maxWidth):
        self.MinHeight = minHeight
        self.MaxHeight = maxHeight
        self.MinWidth = minWidth
        self.MaxWidth = maxWidth

        self.area = [0] * maxWidth
        for x in range(self.MinWidth, self.MaxWidth):
            self.area[x] = [""] * maxHeight

    def Track(self, claim):
        for x in range(claim.FromLeftEdge, claim.FromLeftEdge + claim.Width):
            for y in range(claim.FromTopEdge, claim.FromTopEdge + claim.Height):
                self.area[x][y] = claim.ClaimId if self.area[x][y] == "" else "X"

    
    def NotOverlap(self, claim):
        result = True
        for x in range(claim.FromLeftEdge, claim.FromLeftEdge + claim.Width):
            for y in range(claim.FromTopEdge, claim.FromTopEdge + claim.Height):
                if self.area[x][y] == "X" or self.area[x][y] == "":
                    result = False

        return result
                    

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
    
    # create the cloth.
    cloth = Cloth(0, 0, maxHeight, maxWidth)

    # build up the cloth
    for claim in claims:
        cloth.Track(claim)
    
    for claim in claims:
        if cloth.NotOverlap(claim):
            print(str(claim))

    
    

if __name__ == "__main__":
    main()