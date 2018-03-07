#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

solution = sum(line[4] == "F" for line in vec) #use Boolean for Full-time workers, True = 1 and False = 0; sum number of 1s to get total Full-time

print(solution)
