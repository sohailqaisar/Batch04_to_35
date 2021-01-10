#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x
function1()


# In[8]:


# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))     #wrtie your code here


    return x
function2()


# In[8]:


#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[(a%35==0)] #wrtie your code here
    return x
function3() 
  


# In[77]:


#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    arr[:,[0, 1]] = arr[:,[1, 0]]
  
    # return np.swapaxes[:,[1,2]]#wrtie your code here
    return arr
function4()


# In[9]:


#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros(20,np.int).reshape(4,5)#wrtie your code here
  
    return z
function5()


# In[50]:


#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr = np.zeros(10)#wrtie your code here
    arr[np.array([5,8])]=10,20
    return arr
function6()  


# In[10]:


#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
  
    return np.zeros_like(x) #write your code here
function7()


# In[11]:


#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x=np.full((2,5),6, dtype='uint32')#write your code here
  
    return x
function8()


# In[96]:


#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    
    a = np.arange(2,101,2)# write your code here
    a[a%2==0]
    return a

function9()


# In[14]:


#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt =arr-np.vstack(brr) # write your code here 
  
    return print(subt)
function10()


# In[15]:


#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ans =np.where(arr%2!=0, -1, arr)  #write your code here 
    return ans
function11()


# In[12]:


#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = np.hstack((np.repeat(arr,3),np.tile(arr,3)))#write your code here 
    return ans
function12()


# In[13]:


#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr>5)&(arr<10)]#write your code here 
    return ans
function13()


# In[14]:


#task14
import numpy
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
   
    arr = numpy.arange(10, 34, 1).reshape(8,3)#write reshape code
    ans = numpy.split(arr,4)#write your code here 
    return ans
function14()


# In[15]:


#task15
def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    ans = arr[arr[:,1].argsort()]#write your code here 
  
    return ans
function15()


# In[155]:


#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.dstack((x,y))#write your code here 
  
    return ans
function16()


# In[33]:


#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    return np.where((arr%15==0),'Yes','No')        # Write Your Code HERE
function17()


# In[34]:


#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = len(set(piaic)&set(students))# Write you code Here
    return x
function18()


# In[76]:


# Task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 
    # Now return output as "(X*W)+b:

    X = np.arange(1,26).reshape(5,5)# Write your code here
    W = X.copy()# Write your code here 
    W = W.T# Write your code here
    b= 5
    output = (X*W)+b# Write your code here
    return output
function19()


# In[74]:


#Task20
def fucntion20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def xyz(x):
        return x*2+3-2

    return xyz(x)#Write your Code here
fucntion20()

