import pandas as pd 

#Another example of tidying datasets where column headers are values
billboard_data = pd.read_csv('billboard.csv')
#A larger wide data problem
billboard_data.head()

#Using Melt function

billboard_data = pd.melt(
    billboard_data,
    id_vars=['year','artist','track','time','date.entered'],
    var_name ='week',
    value_name='rating')

billboard_data.head()
billboard_data.shape