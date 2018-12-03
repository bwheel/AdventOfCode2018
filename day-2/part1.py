#!/usr/bin/env python

doubles =  0
triples = 0

with open("input.txt") as f:
    for line in f:
        letters = {}
        id = list(line)
        # hash up the id
        for letter in id:
            if letter in letters:
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1
        
        # if we have atleaset one double we count it, but no more than one.
        for k in letters:
            if letters[k] == 2:
                doubles = doubles + 1
                break
        
        # if we have atleast one triple, we count it, but no more than one. 
        for k in letters:
            if letters[k] >= 3:
                triples = triples + 1
                break

result = doubles * triples

print(result)