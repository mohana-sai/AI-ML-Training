#!/usr/bin/env python
# coding: utf-8

# # Polynomial Regression

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
import numpy as np

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)


# In[2]:


x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))


# In[3]:


import matplotlib.pyplot as plt

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()


# In[4]:


from sklearn.metrics import r2_score

r2 = r2_score(y, p4(x))

print(r2)

