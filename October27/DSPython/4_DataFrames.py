import numpy as np
import pandas as pd
from numpy.random import randn
# Index Levels
outside = 'G1 G1 G1 G2 G2'.split()
# print(outside)
inside = [1, 2, 3, 1, 2, 3, 4, 5, 6]
hier_index = list(zip(outside, inside))
#print(hier_index)
#print(pd.MultiIndex.from_tuples(hier_index))
#print(pd.MultiIndex.from_tuples(hier_index)) #levels are how indexs are agreggated to eachother
                                             #labels are integers given to row or column values
hier_index = pd.MultiIndex.from_tuples(hier_index)
#print(hier_index)
df = pd.DataFrame(randn(5, 2), hier_index, ['A', 'B']) #Creates dataframe using multiIndex, sets
                                                       #Sets two columns and creates random values
#print(df)
#print(df.loc['G1']) #Prints all labels associated with G1
#print(df.loc['G1'].loc[1]) #Prints all labels associated with G1 and prints row at index 1
#print(df.index.names)  #Prints name associated to each index
df.index.names = ['Groups', 'Num']  #Sets name of each index
#print(df.index.names)
print(df)
#print(df.loc['G2'].loc[2]['B']) #Print all lables associated with G2 and prints row at index 2 and col B

#print(df.xs('G1'))
print(df.xs(3, level='Num')) #Prints all rows where Num index is equal to 1
