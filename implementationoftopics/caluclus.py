#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[9]:


import sympy as sym
x, y, z = sym.symbols('x y z')
 
# expression of which we have to find derivative
exp = x**5 * y + y + z
 
# Differentiating exp with respect to x
derivativex = sym.diff(exp, x)
print('derivative with respect to y ',derivativex)


# In[11]:


derivativey = sym.diff(exp, y)
print('derivative with respect to y : ',derivativey)


# In[13]:


derivativex = sym.diff(exp, x, 2)
print('second derivative with respect to x: ',
      derivativex)


# In[14]:


derivativey = sym.diff(exp, y, 2)
print('second derivative with respect to y: ', derivativey)


# In[17]:


integral = sym.integrate(sym.tan(x), x)
print('indefinite integral of tan(x): ',
      integral)


# In[18]:


integral2 = sym.integrate(sym.cot(x), (x, -1, 1))
print('definite integral of cot(x) between -1 to 1: ',
      integral2)


# In[19]:


integral3 = sym.integrate(sym.exp(-x), (x, 0, sym.oo))
print('definite integral of exp(-x) between 0 to ∞: ',
      integral3)


# In[ ]:




