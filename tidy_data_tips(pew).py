import pandas as pd 

#Reference and practicing how to tidy data from author: Hadley Wickham
#https://vita.had.co.nz/papers/tidy-data.pdf


#Case 1: Tyding Data where Columns Headers are Values instead of name
pew_data = pd.read_csv("pew.csv")

#Check proper import of data at a glance
pew_data.head()

'''
Hadley Wickham mentions that we can observe 3 variables. 
Namely: Religion, Income and Frequencies

Daniel Chen (pycon2018) also mentions that this is 'wide format' data

"Melt" or "Stack" the dataset to tidy it. 
This means turn the columns into rows
'''


#Using the melt function 
'''
melt(frame, id_vars=None, 
value_vars=None, 
var_name=None, value_name="value", col_level=None)

frame = dataset 
id_vars = column which we want to hold/dont want to touch
This melts all the columns as well.
'''
#id_vars parameter
pd.melt(pew_data,id_vars='religion',var_name='income',value_name='frequency')

'''
We see that a new column called variable is created.  
The original column header now becomes the observation 
'''



