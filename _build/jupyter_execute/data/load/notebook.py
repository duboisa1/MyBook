#!/usr/bin/env python
# coding: utf-8

# ## Notebook

# In[11]:


from iepy.load import get_load
get_load(countries=["BE"], years_range=[2018, 2018]).plot()

