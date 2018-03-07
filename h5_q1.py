#!/usr/bin/env python

import pandas as pd

#chmod u+rwx q1.py

df = pd.read_csv('chicago_crime.csv')

grouped = df.groupby('Primary Type')['Arrest'].mean().sort_values(ascending = False)
#take the mean of each primary type taking TRUE as 1 for Arrest and 0 as FALSE

temp = grouped.head(1)

solution = temp.index.values

print(solution)
