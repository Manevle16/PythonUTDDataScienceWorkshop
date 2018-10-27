import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A B C D E'.split()],['W','X','Y','Z'])
print(df)
#print(df>0) #Returns dataframe of true/false values relating to expression
#print(df[df>0]) #Returns dataframe of values that are True and NaN that are false
#print(df['W'] > 0) #Returns series of True/False values relating to expression
resultDf = df[df['Z'] < 0] #Returns rows where column Z value is less than 0
#print(resultDf)
resultDf = df[df['Z'] < 0][['X','Y']]  #Returns rows where column Z value is less than 0 of only
                                       #columns X and Y
#print(resultDf)
boolser = df['W'] > 0 #Get rows where column W value is greater than 0 as T/F values
result = df[boolser] #Print rows in dataframe
#print(result)

#print(df[(df['W']>0) & (df['Y']>1)]) #Return rows where column W > 0 and column Y > 1
#print(df.reset_index()) #Returns dataframe with row labels converted into values
#df.reset_index(inplace=True) #Sets dataframe's row labels converted into values

newInd = 'CA NY WY OR CO'.split()
#print(newInd)
df['States'] = newInd #Creates new column called states with row values of newInd
print(df)

df.set_index('States')
df.set_index('States', inplace=True)
print(df)
