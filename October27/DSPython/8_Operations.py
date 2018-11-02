import numpy as np
import pandas as px

df = px.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [None, 555, 666, 444],
                   'col3': 'abc def ghi xyz'.split()})
#print(df)
#print(df.head(2)) #returns first 2 rows
#print(df['col2'].unique()) #returns all unique values in given column
#print(df['col2'].value_counts()) #returns series showing count of each value in given column
#print(df[(df['col1'] > 2) & (df['col2'] >= 444)]) #returns all rows that is true for the statement

#apply method


def times2(x):
    return x*2


#print(df['col1'].sum()) #Returns sum of col1
#print(df['col1'].apply(times2)) #Applys function to each value in given column
#print(df['col3']) #Print all values in given column
#print(df['col3'].apply(len)) #Print len of each value of every column
#print(df['col2'].apply(lambda x: x*2)) #Print all values of given column multiplied by two

#print(df.drop('col1', axis=1))  #remove given column from dataframe
#print(df.columns) #return columns names
#print(df.index) #returns index count and the way it steps through it

#print(df.sort_values('col2', ascending=False))  #Sorts values by given column in descending order
#print(df.isnull()) #Checks if value in column is a null

data = {'A': 'foo foo foo bar bar bar'.split(),
        'B': 'one one two two one one'.split(),
        'C': 'x y x y x y'.split(),
        'D': [1, 3, 2, 5, 4, 1]}
#print(data)

df = px.DataFrame(data)
print(df)
print()
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C'])) #Pivots table using index to define indexs, columns to define columns, values to define
                                                                   #what values will be used
