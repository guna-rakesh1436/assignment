#!/usr/bin/env python
# coding: utf-8

# In[2]:


def pos(n):
    return n[-1]  
def sort(tuples):
    return sorted(tuples, key=pos)
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort(a))


# In[ ]:




