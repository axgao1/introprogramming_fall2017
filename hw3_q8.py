#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

firelist = [line for line in vec if line[3] == "FIRE"] #returns lists of those with FIRE DEPARTMENT in 4th position

sortedfirelist = sorted(firelist, key = lambda x:x[7]) #sort list based on Annual Salary using lambda function

if len(sortedfirelist) % 2 == 0: #if list length is even:
    #tempmed = [sortedfirelist[len(sortedfirelist)/2], sortedfirelist[int(len(sortedfirelist)/2)+1]]
    med1 = sortedfirelist[(len(sortedfirelist)/2)-1] #obtains the first of the two lists in the middle of sortedfirelist
    med2 = sortedfirelist[(len(sortedfirelist)/2)] #obtains the second of the two lists in the middle of sortedfirelist
    medsalary = (med1[7] + med2[7]) / 2 #add the 8th value, Annual Salary, in both lists and divide by 2 for median salary of sortedfirelist

else: #if list length is odd:
    tempmed = sortedfirelist[int(len(sortedfirelist)/2)] #if length is odd, divide by 2 and convert result to integer, taking list 1 position back
    medsalary = tempmed[7] #element in 8th position of resulting list is median salary of sortedfirelist

solution = medsalary

print(solution)
