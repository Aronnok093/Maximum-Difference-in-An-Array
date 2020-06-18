#!/usr/bin/env python
# coding: utf-8

# In[7]:


array=list(map(int,input("Enter Numbers Using space: ").split()))
array.sort()
size=len(array)
sum_a=0
sum_b=0
for i in range(int(size/2),size):
    sum_a=sum_a+array[i]
for i in range(0,int(size/2)):
    sum_b=sum_b+array[i]
print("Maximum Difference Is: ",sum_a-sum_b)

