#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

hourlylist = [line for line in vec if line[5] == "Hourly"] #if 6th position in each list is "Hourly", return list

sortedhourlylist = sorted(hourlylist, key=lambda x:x[8], reverse = True) #used lambda function to sort hourlylist by hourly rate in descending order

solution = sortedhourlylist[3][8] #starts with 4th list and takes 9th element in list

print(solution)
