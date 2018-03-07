#!/usr/bin/env python

import pandas as pd

#chmod u+rwx q2.py

df = pd.read_csv('chicago_crime.csv')

grouped = df.groupby('Ward')['Primary Type'].count().sort_values(ascending = False)
#count the Primary Types of each ward

temp = grouped.head(1)

solution = temp.index.values

print(solution)
