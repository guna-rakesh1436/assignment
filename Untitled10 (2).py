#!/usr/bin/env python
# coding: utf-8

# In[3]:


def count(str):
    upper = lower = 0
    for char in str:
        if char.islower():
            lower+=1
        else:
            upper+=1
    print('Number Of Uppercase Letters:',upper)
    print('Number Of Lowercase Letters:',lower)
string = input()
count(string)


# In[ ]:




