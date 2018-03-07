#!/usr/bin/env python

# You can simply write your final solution as a comment.

import pandas as pd

data = pd.read_csv("chicago_schools.csv", usecols=['ISBE_ID', 'PARCC Proficiency (%)', 'College Ready (%)', \
                                                    'Ready for Next', 'Low Income (%)'])

data.dropna(inplace = True)

chartermask = data[data['ISBE_ID'].str.contains('C')] #contains C for charter schools
publicmask = data[~data['ISBE_ID'].str.contains('C')] #the opposite, does not contain C

charter_crmed = chartermask.median()['College Ready (%)'] #median college ready % for charter schools
public_crmed = publicmask.median()['College Ready (%)'] #median college ready % for public schools

solution = (charter_crmed, public_crmed)

print(solution) #comparing medians of college readiness % between charter and public schools

charter_limed = chartermask.median()['Low Income (%)']
public_limed = publicmask.median()['Low Income (%)']

lowincomemed = (charter_limed, public_limed)

print(lowincomemed) #comparing medians of low income % between charter and public schools

#The median charter school has 94.45% low income students.
#The median public school has 94.9% low income students.
#Charter and public schools serve comparable percentages of low income students,
#so if basis of comparison was based on % of low income, then comparing apples-to-apples.
#However, there could be other factors that make charter and public schools not comparable.
