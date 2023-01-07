import matplotlib.pyplot as fig
import datetime as dt
import pandas_datareader.data as web


inicio = dt.datetime(2019,1,1)
fim = dt.datetime(2019,11,24)
df = web.DataReader('PETR4.SA','yahoo',inicio,fim)
df['Close'].plot(color='k',lw=4)
fig.grid()
fig.title('PETR4 (Jan-Nov / 2019)',fontsize=18,weight='bold')