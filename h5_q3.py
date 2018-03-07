#!/usr/bin/env python

import pandas as pd

dfdates = pd.read_csv('chicago_crime.csv', parse_dates = ['Date'])

dfdates['Week'] = dfdates['Date'].dt.dayofweek * 24 #number that goes from 0-6 multiplied by 24 hours
dfdates['Hour'] = dfdates['Date'].dt.hour #hours 0-24 to be added for hours in 1 day
dfdates['conthours'] = dfdates['Hour'] + dfdates['Week'] #total hours lapsed since Monday 12:00am for
                                                        #a total of 7 days with 24 hours each resulting
                                                        #in a total of 168 hours

graph = dfdates['conthours'].plot(kind = "hist", bins = 168)

graph.set_xlabel("Continuous Hours Since Monday Midnight")
graph.set_ylabel("Frequency of Crime")

graph.figure.savefig('q3.pdf')
