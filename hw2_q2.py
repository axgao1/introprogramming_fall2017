#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.

solution = 0
max_fib  = 1e9

allfibs=[]
a , b = 1 , 1

while b < 1000000000:
    c = a + b #creates new variable to hold third value of the Fibonacci sequence.
    a = b #replacing old value with new value
    b = c
    if a % 17 == 0: #chose a to be divisible by 17 because a becomes original b
                    #and original b becomes c, which is over 1e9
        allfibs.append(a) #add each a divisible by 17 to list
solution = sum(allfibs)
print(solution)

# Check for the correct answer.
if max_fib == 1e9:
  print("#2 : Fibonacci ::", "Correct." if solution == 15129388 else ("Wrong: " + str(solution)))
