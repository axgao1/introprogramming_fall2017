#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0
max_start = 2000000

# Your code goes here.
# Should be < 10 lines.

# create a function that returns
# the next value in the collatz sequence.

def collatz(n):
  if n%2: return 3*n + 1
  else:   return int(n/2)
link = collatz(link)




def function_collatz(n):
    while n > 1:



# now loop up to 2 million,
# tracking the longest sequence

# Double bonus: precompute!
# If you reach 13, for instance, you're always 9 steps from the end,
# and you don't need to calculate it all over again.

# Check for the correct answer.
if max_start == 2000000:
  print("#7 : Collatz Sequence ::", "Correct." if solution == 1723519 else ("Wrong: " + str(solution)))
