
import pandas_datareader.data as web
import datetime
 
symbol = []
with open('files/stock_list.txt') as f:  
    for line in f:
        symbol.append(line.strip())
f.close
 
end = datetime.datetime.today()
start = datetime.date(end.year-5,1,1)

i=0
while i<len(symbol):
    try:
        df = web.DataReader(symbol[i], 'yahoo', start, end)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        df['Close_Delta'] = df.Close.diff()
        df['Pct_Change'] = df.Close.pct_change()
        df = df.round(2)
        if i == 0:
            df.to_csv('files/tickers_loop.csv')
            print (i, symbol[i],'has data exported to csv')
        else:
            df.to_csv('files/tickers_loop.csv',mode = 'a',header=False)
            print (i, symbol[i],'has data exported to csv.')
    except:
        print("Error in script or no data found.")
        print (i,symbol[i])
        continue
    i=i+1
    