#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

policelist = [line for line in vec if line[3] == "POLICE"] #if 4th position (Department) in each list is "POLICE", return list; creates new list containing just those in POLICE DEPARTMENT

deteclist = [x for x in policelist if "DETECTIVE" in x[2]] #from new list of just those in POLICE DEPARTMENT, if 3rd position (Job Titles) include "DETECTIVE", return list.

solution = len(deteclist) #number of lists in list of detectives

print(solution)
