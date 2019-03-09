#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_excel('Shares.xlsx')


# In[4]:


companies = list(data.columns)


# In[6]:


company_dict = dict()
for i in companies:
    company_dict.update({i:[data[i]['Average Stk price']]*4+[0,(1/(data[i]['Revenue']*data[i]['Shareholders Equity per Share']))]})


# In[8]:


l = list()
for i in company_dict:
    l.append(company_dict[i][5])   


# In[9]:


for i in company_dict:
    company_dict[i][5] = (company_dict[i][5]-min(l))/(max(l)-min(l))


# In[11]:

name = []
current=[]
pct_change=[]


def VF(company_Parameters):
    for i in company_Parameters:
        name.append(i)
        current.append(company_Parameters[i][0])
        pct_change.append(company_Parameters[i][4])


# In[12]:


VF(company_dict)


# In[15]:


import time, random
while True:
    frontEnd_return=[]
    time.sleep(5)
    for i in range(9):
        with open('current.txt') as f:
            s = [(i.replace('\n','')).split() for i in f.readlines()]
        nm = name[i]
        prev = current[i]
        current[i] = float(s[i][1])
        current[i] *= random.uniform(0.95,1.05)
        pct_change[i] = ( (current[i] - prev) / current[i] ) * 100.0
        frontEnd_return.append([nm,round(current[i],2),pct_change[i]])
        with open('values.txt','w') as f:
            for j in frontEnd_return:
                s = ""
                for k in j:
                    s = s+str(k)+" "
                f.writelines(s+"\n")
    print(frontEnd_return)
    print("\n")


# In[ ]:




