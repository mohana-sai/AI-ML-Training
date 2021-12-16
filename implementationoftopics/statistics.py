#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Mean calculation
import numpy as np
a =[11, 21, 34, 22, 27, 11, 23, 21]
mean = np.mean(a)
print (mean)


# In[6]:


#Median
a =[11, 21, 34, 22, 27, 11, 23, 21]
print(np.median(a))


# In[4]:


#Mode
from scipy import stats

a =[11, 21, 34, 22, 27, 11, 23, 21]
print (stats.mode(a)[0][0])


# In[8]:


#Standarddevviation
a =[11, 21, 34, 22, 27, 11, 23, 21]
print (np.std(a))


# In[ ]:




