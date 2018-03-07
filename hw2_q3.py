#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0
number   = 175832868806

primelist = []
max = 301
a = 2
counter = 0 #sets up counter to keep track of number of primes

for n in range(a, max): #starts with first prime number, 2
    for i in range(2, n):
        if n % i == 0: #if any number between 2 and 300 is divisible by any
                        #other number between 2 and that number itself
            break #if divisible, it's not prime so exit and loop to next n
    else: primelist.append(n) #creates a list of prime numbers up to 300

for pf in primelist:
    if number % pf == 0:
        counter += 1 #1 gets added to the counter each time the long number is
                     #divisible by one of the prime numbers in the list

solution = counter
print(solution)


# Check for the correct answer.
if number == 175832868806:
  print("#3 : Count Prime Factors ::", "Correct." if solution == 6 else ("Wrong: " + str(solution)))
