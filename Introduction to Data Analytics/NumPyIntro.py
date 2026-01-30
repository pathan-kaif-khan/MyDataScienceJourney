import numpy as np
# 1D array
array1 =np.array([10,20,30])
print(array1)

print(type(array1))

array2=np.array([5,-7.5,'a',7.2])
print(array2)
print(type(array2))

#2D array
array3 = np.array([[2.4,3],[4.91,7],[0,-1]])
print(array3)
print(type(array3))

#Attributes of python array
print("number of dimensions of array1",array1.ndim)
print("number of dimensions of array3",array3.ndim)
# ndarray.shape attribute
print("number of shape of array1",array1.shape)
print("number of shape of array2",array2.shape)
print("number of shape of array3",array3.shape)
# ndarray.size attribute
print("number of size of array1",array1.size)
print("number of size of array2",array2.size)
print("number of size of array3",array3.size)
# ndarray.dtype attribute
print("number of dtype of array1",array1.dtype)
print("number of dtype of array2",array2.dtype)
print("number of dtype of array3",array3.dtype)
# ndarray.itemsize attribute
    #memory allocated to integer,string,float as follows
print("number of itemsize of array1",array1.itemsize)
print("number of itemsize of array2",array2.itemsize)
print("number of itemsize of array3",array3.itemsize)

#other ways to create numpy
array4 = np.array( [ [1,2], [3,4] ], dtype=float)
print("element of array4",array4)
print("datatype of array4",array4.dtype)

#using zeroes function
array5=np.zeros([3,3])
print(array5)
#using ones function
array6=np.ones((3,4))
print(array6)
#using arange function
array7=np.arange(30)
print(array7)

array8=np.arange(-3,8,3)
print(array8)

#create an array of 4rows and 3columns
array9=np.array([[78,67,56],[76,75,47],[84,59,60],[67,72,54]])
print(array9)
array10=np.ones((4,3))
print(array10)
array9[0,0]=99
print(array9)
"""print("enter the no. of rows",i)
marks=([i,j])
print("enter the no. of columns",j)"""

#slicing
# array[start:end:step]
array10=np.array([-2, 2, 6, 10, 14, 18, 22])
print(array10[3:5])
print(array10[::-1])
#slicing 2D array
array11=np.array([[ 1, -4, 7,  10],
                   [ 2,  5, 8, -11],
                   [ 3, -6,  9,  12]])
#array11[start_row : stop_row , start_col : stop_col]
print(array11)
print(array11[1:3,0:3])





