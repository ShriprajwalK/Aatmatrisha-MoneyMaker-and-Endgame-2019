#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

with open('current_endgame.txt') as f:
	main = [(i.replace('\n','')).split() for i in f.readlines()]
	
company_dict = {i[0]:i[1:] for i in main}

name = []
current=[]
pct_change=[]


def VF(company_Parameters):
    for i in company_Parameters:
        name.append(i)
        current.append(float(company_Parameters[i][0]))
        pct_change.append(float(company_Parameters[i][1]))


# In[12]:


VF(company_dict)


# In[15]:


import time, random
while True:
    frontEnd_return=[]
    time.sleep(5)
    for i in range(18):
        with open('current_endgame.txt') as f:
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




