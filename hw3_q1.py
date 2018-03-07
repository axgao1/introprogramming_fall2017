#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

solution = len(vec) #each list in vec represents one person, the length of vec is the number of lists/people

print(solution)
