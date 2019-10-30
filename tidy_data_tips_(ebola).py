import pandas as pd 

##Tidying data 
#Reference from Daniel Chen Pydata(2018)
#This is still in progress. Will update along the way

'''
Let's see how we can make the dataset less 'wide' but 'long'?
We see that there are many repeats of similar records.
Can we somehow change this to record date,day,country, deaths clearly?
'''

ebolas_data = pd.read_csv('country_timeseries.csv')

ebola_long = pd.melt(ebolas_data,id_vars=['Date','Day'],)
ebola_long.head()

'''
Holding Date and Day results in something we would want. 
But we realise that the countries count,death lumped together 
'''

