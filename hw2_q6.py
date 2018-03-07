#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 1
N = 101

for i in range(1,N):
    solution = solution*(i + 100)//i #simplified factorials to 1 to 200 in the
                                    #numerator and 1 to 100 in the denominator.
                                    #division is 101/1 x 102/2 x 103/3 ... 200/100.
print(solution)


# Check for the correct answer.
if N == 101:
  print("#6 : Grid ::", "Correct." if solution == 90548514656103281165404177077484163874504589675413336841320 else ("Wrong: " + str(solution)))
