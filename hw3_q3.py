#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

solution = sum(line[4] == "P" for line in vec) #for Part-time workers, True = 1 and False = 0; sum number of 1s to get total Part-time
print(solution)

total = sum(line[4] == "F" for line in vec) + sum(line[4] == "P" for line in vec) #add up Full-time and Part-time workers, since all workers are labeled either, to get total workers
print(total)

if total == len(vec): #total numer should be same as result from q1
    print("Yes!") #print confirmation
