#Group by chosen dataframe index to navigate and pull information out of the data
import numpy as np
import pandas as pds

company = 'GOOG GOOG MSFT MSFT FB FB'.split()
person = 'Sam Charlie Amy Vanessa Carl Sarah'.split()
sales = [200, 120, 340, 124, 243, 350]
data = {'Company': company, 'Person': person, 'Sales': sales}
#print(data)
df = pds.DataFrame(data)
#print(df)
#print(df.groupby('Company'))
byComp = df.groupby('Company') #Group datafram by Company
#print(byComp.mean())
#print(byComp.std())
#print(byComp.sum())
#print(byComp.sum().loc['FB']) #Get sums of groups of row FB
#print(byComp.count()) #Count rows related to each group
# print(byComp.min()) #Gets minimum value of each group
# print(byComp.max())
#print(byComp.describe()) #Gives count, mean, std, min, 25%, 50%, 75%, and max
print(byComp.describe().transpose()['FB']) #Describes row FB
