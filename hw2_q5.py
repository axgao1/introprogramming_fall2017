#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# You could use here the square root function, sqrt.
# It returns a floating point value
# sqrt(9) -> 3.0 but sqrt(10) -> 3.162...
# But... you don't need it!

for a in range(0,1000):
    for b in range(a,1000): #for a Pythagorean triple, b has to be larger than a (when a already started in first position) so range starts with a.
        c = 1000 - b - a
        if a*a + b*b == c*c: #a^2+b^2=c^2
            solution = a*b*c
            print(solution)
            break


# Check for the correct answer.
print("#5 : Pythagorean Triplet ::", "Correct." if solution == 31875000 else ("Wrong: " + str(solution)))
