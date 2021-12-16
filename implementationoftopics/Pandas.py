#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
df = pd.read_csv("PastHires.csv")
df.head(11)


# In[2]:


df.head(10)


# In[3]:


df.tail(4)


# In[4]:


df.shape


# In[5]:


df.size


# The len() function gives you the number of rows in a DataFrame:

# In[6]:


len(df)


# In[7]:


df.columns


# In[8]:


df['Hired']


# In[9]:


df['Hired'][:5]


# In[10]:


df['Hired'][5]


# In[11]:


df[['Years Experience', 'Hired']]


# In[12]:


df[['Years Experience', 'Hired']][:5]


# In[13]:


df.sort_values(['Years Experience'])


# In[14]:


degree_counts = df['Level of Education'].value_counts()
degree_counts


# In[15]:


degree_counts.plot(kind='bar')

