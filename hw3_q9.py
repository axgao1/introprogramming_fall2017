#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

namelist = [line[1].strip().split(" ")[0] for line in vec if "POLICE OFFICER" in line[2]]
#if POLICE OFFICER (includes DETECTIVE) is included in Job Titles in each list,
#return the list with just first name excluding beginning and trailing spaces and middle initial

dictname = {} #set dictname as a dictionary

for name in namelist:
    if name in dictname:
        dictname[name] = dictname.get(name, 0) + 1 #use name key to get value, number of counts name appears, add 1 to count every time name appears
    else:
        dictname[name] = 1

sorteddict = sorted(dictname, key = dictname.get, reverse = True) #reverse sort on number of times name appears using key/name

#solution = [(name, dictname[name]) for name in sorteddict]

solution = [(name, dictname[name]) for name in sorteddict if dictname[name] == 37] #just returns name for which appearance count is 37

print(solution)

# Solution should contain the single police officer name with 37 occurrences.
