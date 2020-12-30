#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[2]:


import numpy as np


# 2. Create a null vector of size 10 

# In[7]:


empty_arry=np.empty(10)
empty_arry


# 3. Create a vector with values ranging from 10 to 49

# In[9]:


arang_arr=np.arange(10,50)
arang_arr


# 4. Find the shape of previous array in question 3

# In[10]:


np.shape(arang_arr)


# 5. Print the type of the previous array in question 3

# In[11]:


type(arang_arr)


# 6. Print the numpy version and the configuration
# 

# In[333]:


print( np.__version__ )

print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[334]:


np.ndim(arang_arr)


# 8. Create a boolean array with all the True values

# In[335]:


bool_arr = np.ones(10, dtype=bool)
bool_arr


# 9. Create a two dimensional array
# 
# 
# 

# In[336]:


arr2d = np.arange(20).reshape(4,5)
arr2d


# 10. Create a three dimensional array
# 
# 

# In[337]:


arr3d = np.arange(27).reshape(3,3,3)
arr3d


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[338]:


arang_arr[::-1]


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[340]:


import numpy as np
x = np.empty(10)
x[5] = 1
print(x)


# 13. Create a 3x3 identity matrix

# In[50]:


np.identity(3)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[343]:


arr = np.array([1, 2, 3, 4, 5] ,np.float)
arr


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[344]:


arr1 = np.array([[1., 2., 3.], [4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr1*arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[345]:


arr1 = np.array([[1., 2., 3.],

            [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.],
            [7., 2., 12.]])
arr3 =arr1==arr2
arr3


# 17. Extract all odd numbers from arr with values(0-9)

# In[361]:


arr=np.arange(0,10) 
arr=arr[arr%2!=0]
arr


# 18. Replace all odd numbers to -1 from previous array

# In[362]:


arr[::]=-1
arr


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[363]:


arr = np.arange(10)
arr[5:9:]=12
arr


# 20. Create a 2d array with 1 on the border and 0 inside

# In[364]:


arr=np.ones(25,np.int).reshape(5,5)
arr
arr[1:-1,1:-1]=0
arr


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[365]:


arr2d = np.array([[1, 2, 3],

            [4, 5, 6], 

            [7, 8, 9]])
arr2d[1:-1,1:-1]=12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[366]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[:1]=64
arr3d


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[367]:


arr=np.arange(10).reshape(5,2)
arr[:1]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[368]:


arr=np.arange(10).reshape(5,2)
arr[1:2]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[369]:


arr=np.arange(10).reshape(2,5)
arr[:,3:4]



# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[372]:


arr=np.array(np.random.randn(10,10)*10,dtype=np.int)
print(arr.max())
print(arr.min())


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[373]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a, b))


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[375]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a==b)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[376]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
mask=(names!="Will")
data[mask]


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[377]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
mask=((names!="Will") & (names!="Joe"))
data[mask]


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[378]:


arr=np.arange(1,16).reshape(5,3)
arr


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[379]:


arr3d=np.arange(1,17).reshape(2, 2, 4)
arr3d


# 33. Swap axes of the array you created in Question 32

# In[231]:


np.transpose(arr3d)


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[380]:


arr=np.array(np.random.randn(10))
arr[arr<.5]=0
arr=np.sqrt(arr)
arr


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[381]:


x=np.array(np.random.randn(12))
y=np.array(np.random.randn(12))
print (x)
print (y)
np.maximum(x, y)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[382]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names
np.sort(np.unique(names))


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[281]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
np.setdiff1d(a, b)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[318]:


import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = numpy.array([[10,10,10]])

sampleArray[:,2:3]=numpy.transpose(newColumn)

sampleArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[319]:


x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(y,x)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[330]:


my_array=np.array(np.random.randn(20),dtype=np.int)
numpy.matrix.cumsum(my_array)

