import matplotlib as mp
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader.data as web
import yfinance as yf

yf.pdr_override()

df = web.get_data_yahoo('PETR4.SA',start='2019-01-01',end='2019-11-24')
df['Close'].plot(color='black',lw=4)
plt.grid()
plt.title('PETR4 (Jan-Nov/2019)',fontsize=16,weight='bold')
plt.show()
print(df['Close'].head(5))


import seaborn as sns
import numpy as np
import pandas as pd
df1=web.get_data_yahoo('GGBR4.SA',start='2019-01-01',end='2019-11-24')
df1['Data']=df1.index
df2=web.get_data_yahoo('PETR4.SA',start='2019-01-01',end='2019-11-24')
df2['Data']=df2.index

data = {'petro': df1['Close'],
        'ggb': df2['Close'],
        }
df = pd.DataFrame(data)

dados=sns.regplot(x="petro",y="ggb",data=df,scatter_kws={'color':'red'},line_kws={'color':'blue'})
dados.set_xlabel('PETR4',fontsize=16)
dados.set_ylabel('GGBR4', fontsize=16)
dados.grid()
plt.title('PETR4 X GGBR4 - Relação (Jan-Nov/2019)',fontsize=14,weight='bold')
plt.show()

dad_conj=sns.jointplot(x="petro",y="ggb",data=df,kind='scatter')
dad_conj.set_axis_labels('PETR4','GGBR4',fontsize=16)
plt.show()