import pandas as pd 
import matplotlib 
#read csv using read_csv() method
dataframe = pd.read_csv("avocado.csv")

#head() method diplays first 5 rows of csv
print(dataframe.head())

#tail() method diplays last 5 rows of csv
print(dataframe.tail())

#referencing a specific column by calling the header name
print(dataframe["AveragePrice"].head())

#A new data frame sorted by the 'region' only
albany_df = dataframe[dataframe['region'] == 'Albany']
print(albany_df.head())
print(albany_df.tail())

#Customise the index to be something more meaningful instead of numbers
albany_df.set_index("Date", inplace = True)
print(albany_df.head())

#plot() method from matplotlib
albany_df.plot()


