"""
A walkthrough of what I have learn of Pandas library. 
Collated from various source

"""

#Standard notations 
import pandas as pd 

#Indicating the desired separator parameter from .read_csv() 
#Since it is a tab-separated-value file, we indicate the separator for the method to parse
df = pd.read_csv('gapminder.tsv', sep = '\t')

'''Typically, after reading data. We check! 
using head() ensures helps to check that all columnns are loaded at a glance
default shows 5 values. But we can specify it'''

df.head() 

'''
Reading a file results in a data structure type called 'dataframe'
It two-dimensional labeled array with columns of potentially different types. 
A dataframe can be seen as an indexed two-dimensional NumPy array
Or sometime like a SQL table or CSV format 

Therefore there are ROWS AND COLUMNS
Index = ROWS 
Columns = COLUMS
Body = Data of the table

'''

#To access or find into about columns, we call
#The results shows us the column names
df.columns

#To access or find rows, we call 
#The results shows us number of indexes (rows)
df.index 

#To access Body/Values
df.values

'''There a a few typical steps we take after importing data
We use these few attritubtes and methods
shape, info, describe
'''

'''
shape describes hows many rows and columns are there
'''
#shape is not a method. do not write in shape()
df.shape

'''
info() tells us the info of the datafram
typically we use info() if our data is not too big.
non-null objects means there are no missing objects.
'''
df.info()

'''
Accessing our information
'''

#Similar to list, the syntax to access information is using []
#Example
country_df = df['country']
country_df.head()
print(type(country_df))

'''
Notice that when we select just a column, we are returned 
a data structure called Series

A series is a essentially a column. It is 1-dimensional
2 or more series makes a Dataframe 
Therefore, a Dataframe is a mutli-dimensional table made up of series
'''

'''
Subset of a a dataframe
'''

'''
Say we are interested in only a few columns, we can specify it
The syntax is that we pass in a list of names into the data frame
In python, a list is denoted as []
We select information of a dataframe using [] as well. 
Thus, this means we should see double []
'''

#Example
#Extracting 3 columns info
subset = df[['country','continent','year']]
subset.head()

'''
What about if we are only interested specific rows? 
There are 2 methods 
'''

'''
Using loc, references the 'character' of the index which 
is automatically created when a dataframe is created
'''
#Example 1
df.loc[2] 

#Example 2, more than 1 row,.
df.loc[[2,0]]

'''
Using iloc, references the index position of the row.
'''
#Example 1
df.iloc[[2,0]]

'''
In this case, we cannot see the difference because the 
character and index is the same
'''

'''
Selecting specified rows and specified columns
or subsetting rows and columns 
'''

#Using loc
'''
Left or comma specifies rows. 
Right of comma specifies columns
'''
#The example shows us taking all rows but only 2 columns. 
subset2 = df.loc[:,['country','continent']]
subset2.head()

'''
Can we do boolean in our arguments in our rows and cols? We can!
'''

#Example 
#Row filter using year == 1967
#Column filter year and continent
df.loc[df['year'] == 1967,['year','continent']]

#Example 2
'''
Multiple boolean arguments. Wrap the boolean using ()
'''

df.loc[(df['year'] == 1967) & (df['pop'] > 1_000_000),['year','continent']]

'''
Another way of conditional selection 
We can examples of OR selection in 2 ways
'''
#Example (Default)

df[(df['year'] == 1967) | (df['year'] == 1957)]

#Example (using isin() method)
df[df['year'].isin(['1967','1957'])]

