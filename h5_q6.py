#!/usr/bin/env python

import pandas as pd

data = pd.read_csv('bls_unemployment.csv', index_col = 'Date', parse_dates = ['Date'])

ax = data.plot()

ax.set_xlabel("Date")
ax.set_ylabel("Unemployment Rate")

ax.figure.savefig('q6.pdf')

#OVERALL DECLINING UNEMPLOYMENT IN CHICAGO SINCE 2013
