#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

policelist = [line for line in vec if line[3] == "POLICE"] #if 4th position (Department) in each list is "POLICE", return list

solution = len(policelist) #length of new list is number of employees in POLICE DEPARTMENT

print(solution)
