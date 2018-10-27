#built on numpy array
#series hold different object types
import numpy as np
import pandas as pd
labels = ['a', 'b', 'c'] #list object
my_data = [10,20,30] #list object
arr = np.array(my_data)
#print(arr)
d = {'a':10,'b':20,'c':30} #dictionary
#print(d)

#print(pd.Series(data=my_data)) #Make panda series
#print(pd.Series(data=my_data, index=labels)) #Make panda series with index
#print(pd.Series(my_data, labels))
#print(pd.Series(arr, labels))
#print(pd.Series(d))
#print(pd.Series(data=labels))
#print(pd.Series([sum, print, len]))

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
#print(ser1)

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
#print(ser2)

#print(ser1['USA'])
print(ser1 + ser2) #Adds values of same keys, NaN given to keys only found in one series

ser3 = ser1 + ser2

#Goes through all values of series
for key in ser1:
    print(key, end=" ")
