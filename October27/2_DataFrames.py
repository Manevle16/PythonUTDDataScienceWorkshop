import numpy as np
import pandas as pd
from numpy.random import randn

#5 rows and 4 columns of random distribution numbers
#print(randn(5,4))

np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A B C D E'.split()],['W','X','Y','Z'])
#print(df)
#print(df['W']) #gives W column
#print(type(df['W']))
#print(df[['W','Z']]) #gives W and Z columns
df['new'] = df['W'] + df['Z']
#print(df['new'])

#df.drop('new') #Won't work, thinks new is columns
#df.drop('new', axis=1) #Returns a new dataframe with dropped column
df.drop('new', axis=1, inplace=True) #Performs action on dataframe
print(df)
#print(df.shape) #Prints number of rows and columns of dataframe
print(df.loc['A']) #Get row with A identifier
print(df.iloc[2]) #Get row at index 2
print(df.loc[:, 'Y']) #Get at column Y
print(df.loc['B', 'Y']) #Get at row B and column Y
print(df.loc[['A', 'B'],['W','Y']]) #Gets rows A and B, and columns W and Y
