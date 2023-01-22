from pandas_datareader import data as pdr
import pandas as pd
import yfinance as yf
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

yf.pdr_override()

symbol = []

with open('stock_list.txt') as f:  
    for line in f:
        symbol.append(line.strip())
f.close
 
end = datetime.datetime.today()
start = datetime.date(end.year-1,1,1)

i=0
data = []

while i<len(symbol):
    try:
        df = pdr.get_data_yahoo(symbol[i], start, end)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        df['Close_Delta'] = df.Close.diff()
        df['Pct_Change'] = df.Close.pct_change()
        df = df.round(2)
        df = df.reset_index()
        df['Date'] = pd.to_datetime(df['Date']).dt.date       
        df['Month'] = df['Date'] + pd.offsets.MonthBegin(-1)      
        print ('The requested data for', symbol[i],'has been recorded.')
    except:
        print("Error in script or no data found.")
        print (i,symbol[i])
        continue
    temp_data = pd.DataFrame(df)
    data.append(temp_data)
    i=i+1

data = pd.concat(data)
data.to_csv('tickers_loop.csv')
print("\n","Data Exported.")
