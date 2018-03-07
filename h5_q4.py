#!/usr/bin/env python

import pandas as pd

from scipy import stats

df = pd.read_csv('chicago_crime.csv')

wmask = df['Primary Type'].str.contains('WEAPON') #creates a mask that contains only WEAPON violations
weapons = df[wmask]
wward = weapons.groupby('Ward').count() #gives the number of weapons violations in each ward
wward['weaponsviocount'] = wward['ID'] #singles out one column since all columns show same numbers
weaponsviocount = wward[['weaponsviocount']] #creates list with both ward ID and weapons violation count for each ward

hmask = df['Primary Type'].str.contains('HOMICIDE') #creates a mask that contains only HOMICIDE
homocides = df[hmask]
hward = homocides.groupby('Ward').count() #gives the number of homicides in each ward
hward['homviocount'] = hward['ID'] #singles out one column since all columns show same numbers
homviocount = hward[['homviocount']] #creates list with both ward ID and homicide count for each ward

joinedwhcounts = weaponsviocount.join(homviocount, how='outer') #join weapons and homicide counts by ward

joinedwhcounts.fillna(0, inplace = True) #fill in with 0 wards (ward 43) with no crime/homicides

x = joinedwhcounts['weaponsviocount']
y = joinedwhcounts['homviocount'] #weapons and homicide columns of joined df

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y) #returns slope, intercept, rvalue, pvalue, stderr

solution = (slope, stderr)

print(solution)
