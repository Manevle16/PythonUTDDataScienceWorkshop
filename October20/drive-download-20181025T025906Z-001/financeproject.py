# Finance Project
# pip install pandas-datareader
import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 1, 9)
BAC = web.DataReader('BAC', 'yahoo', start, end)
print(BAC.tail())
