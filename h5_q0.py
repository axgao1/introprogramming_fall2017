#!/usr/bin/env python

import pandas as pd

df = pd.read_csv('chicago_crime.csv')

grouped = df.groupby('Primary Type')['Arrest'].sum().sort_values(ascending = False)
#sum function marks Arrest being TRUE as 1 and adds up all the 1s. This gives the total number of Arrests.

temp = grouped.head(1)
#highest number after reverse sort.

solution = temp.index.values

print(solution)
