#!/usr/bin/env python
# coding: utf-8

# ### Question1-Solution

# In[1]:


def findProcessors(start, end, n):
    start.sort()
    stop.sort()
    processor_required = 1
    min_processor = 1
    l = 1
    m = 0
    while (l < n and m < n):
        if (start[l] <= stop[m]):
            processor_required += 1
            l += 1
        elif (start[l] > stop[m]):
 
            processor_required -= 1
            m += 1
        if (processor_required > min_processor):
            min_processor = processor_required
 
    return min_processor


# In[2]:


start=[900,940,950,1000,1500,1600]
stop=[910,1020,1010,1015,1620,1700]
n=len(start)


# In[3]:


findProcessors(start, stop, n)


# ### Question 3-Answer

# In[4]:


def deletion_order(data,priority):
    sortf=[]
    sortdate=[]
    if priority=='frequency':
        sortf=sorted(data, key = lambda i: i['frequency'])
        for data in sortf:
            print(data)
    else:
        sortdate=sorted(data, key = lambda i: i['last_updated'])
        for data in sortdate:
            print(data)


# In[5]:


d=[{id:'d1','frequency':7,'last_updated':'18-1-2021'},{id:'d2','frequency':8,'last_updated':'28-1-2021'}]
deletion_order(d,priority='last_updated')


# In[6]:


deletion_order(d,priority='frequency')


# In[ ]:




