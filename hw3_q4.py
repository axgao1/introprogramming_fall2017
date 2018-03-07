#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv") #function call of user-defined function

highhourly = 0

for line in vec:
    if line[8] > highhourly:
        highhourly = line[8] #replace current hourly rate with higher hourly rate when iterating through loop
    solution = highhourly

print(solution)
