# conda install sqlalchemy
# conda install lxml
# conda install html5lib
# conda BeautifulSoup4
# csv excel html sql
import pandas as px
import os
print(os.getcwd())
px.read_csv('./October27/DSPython/google_stock_data.csv')
px.read_csv('./October27/DSPython/911.csv')
df = px.read_csv('./October27/DSPython/911.csv') #Converts csv into a dataframe
#print(df)
#df.to_csv('My_output.csv', index=False) #Outputs csv file of a dataframe
#print(px.read_csv('My_output.csv'))

# pandas cannot import formulas, images, etc.
# conda install xlrd
df = px.read_excel('./October27/DSPython/Excel_Sample.xlsx', sheet_name='Sheet1') #Converts excel document into a dataframe
#print(df)
df.to_excel('./October27/DSPython/Excel_Sample2.xlsx', sheet_name='NewSheet')

data = px.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html') #Convert html table at given link to list of dataframes, dataframe will be stored in first element
#print(type(data))
#print(data[0]) #returns dataframe stored in the list
#print(data[0].head(20)) #returns given amount of rows of dataframe

# sql
from sqlalchemy import create_engine
engine = create_engine('sqlite:///csv_database.db')
df = px.read_csv('./October27/DSPython/Excel_Sample_csv.csv')
print(df)
df.to_sql('my_table', engine, if_exists='replace') #Converts dataframe into sql table
sqldf = px.read_sql('my_table', con=engine) #Returns given table converted into a dataframe
print(type(sqldf))
