#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_excel(r"C:\Quant Club\order book and futures\wipro.xlsx",'wipro')
settle_data= data['Settle Price'].tolist()
settle_data= np.array(settle_data)
spot_price=settle_data[0]

premium = 0





# In[3]:


def payoff(settle_data, premium):
    strike_price_long_gain=spot_price - 1
    
    return np.where(settle_data > strike_price_long_gain, settle_data-strike_price_long_gain,settle_data-strike_price_long_gain) - premium

payoff_long_future = payoff(settle_data, premium)
    


# In[4]:


fig, ax = plt.subplots()
ax.spines['top'].set_visible(False) 
ax.spines['right'].set_visible(False) 
ax.spines['bottom'].set_position('zero') 
ax.plot(settle_data,payoff_long_future,label='long call',color='g')
plt.xlabel('market Price')
plt.ylabel('P/L')
plt.legend()
plt.show()


# In[5]:


def payoff(settle_data, premium):
    strike_price_short_gain=spot_price + 1
    
    return np.where(settle_data > strike_price_short_gain, strike_price_short_gain-settle_data, strike_price_short_gain-settle_data) - premium

payoff_short_future = payoff(settle_data, premium)


# In[6]:


fig, ax = plt.subplots()
ax.spines['top'].set_visible(False) 
ax.spines['right'].set_visible(False) 
ax.spines['bottom'].set_position('zero') 
ax.plot(settle_data,payoff_short_future,label='short call',color='g')
plt.xlabel('market Price')
plt.ylabel('P/L')
plt.legend()
plt.show()

