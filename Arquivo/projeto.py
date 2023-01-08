import matplotlib as mp
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader.data as web
import yfinance as yf

yf.pdr_override()

df = web.get_data_yahoo('PETR4.SA',start='2019-01-01',end='2019-11-24')
df['Close'].plot(color='black',lw=4)
plt.grid()
plt.show()
print(df['Close'].head(5))