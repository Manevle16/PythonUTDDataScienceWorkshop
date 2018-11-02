import numpy as np
import pandas as pd
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
print(d)
df = pd.DataFrame(d)
print(df)
#print(df.dropna()) #Drops all rows with NaN value
#print(df.dropna(axis=1)) #Drops all cols with NaN value
# print(df)
#print(df.dropna(thresh=2)) #Drops all rows with less than 2 NaN values
#print(df)
#print(df.fillna(value=2)) #Replaces all NaN values with 2
print(df.fillna(value=df['A'].mean())) #Replaces all NaN values with the mean of col A
