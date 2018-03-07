#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

highsal = 0

for line in vec:
    if highsal < line[7]:
        highsal = line[7] #replace current salary with higher salary when iterating through loop
        maxperson = line[0] #finds last name of person with highest salary
    solution = maxperson

print(solution)
