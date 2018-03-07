#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0
multiple = 9

i = 1

while (i % 4) or (i % 13) or (i % 14) or (i % 26) or (i % 50): #if any of the modulus values do not equal 0, i not divisible by that number and loop will continue
    i += 1
solution = i*9 #solution*9 is the 9th integer that is a multiple of all specified numbers
print(solution)

# Check for the correct answer.
if multiple == 9:
    print("#1 : 9th Multiple ::", "Correct." if solution == 81900 else ("Wrong: " + str(solution)))
