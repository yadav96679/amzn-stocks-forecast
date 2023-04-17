# -*- coding: utf-8 -*-
"""AMZN stocks forecast.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Ctuzn4R1gEMfiV2itm_EQQlGBBlhMSc
"""

!pip install yfinance

import pandas as pd
import numpy as np
import yfinance as yf

df=yf.download('GOLD',
               start='2000-01-01',
               end='2023-03-07',
               progress=False)

df.head()

df.tail()

df.info()

df.describe()

import matplotlib.pyplot as plt

df['Close'].plot(figsize=(8,5))

df[['Close','Volume']].plot(subplots=True,style='b',
                            figsize=(12,8))

df=pd.DataFrame(df)
df

df['simple_log']=df.Close.pct_change()

df['simple_log']

df['log_rtn']=np.log(df.Close/df.Close.shift(1))

df['log_rtn'].plot()

df['simple_log'].plot()

df['log_rtn'].plot()

df['vlog_rtn']=np.log(df.Volume/df.Volume.shift(1))
df['vlog_rtn']

df.dropna(how='any',axis=0,inplace=True)

corr_coeff=df.log_rtn.corr(df.vlog_rtn)
corr_coeff

import seaborn as sns

corr_coeff=df.log_rtn.corr(df.vlog_rtn)
ax=sns.regplot(x='log_rtn',y='vlog_rtn',data=df)

df['simple_rtn']=df.Close.pct_change()

df['vsimple_rtn']=df.Volume.pct_change()

corr_coeff=df.log_rtn.corr(df.simple_rtn)
corr_coeff

corr_coeff=df.log_rtn.corr(df.simple_rtn)
ax=sns.regplot(x='simple_rtn',y='vsimple_rtn',data=df)

