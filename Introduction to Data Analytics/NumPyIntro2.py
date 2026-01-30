import numpy as np
array1 = np.array([[3,6],[4,2]])
array2 = np.array([[10,20],[15,12]])
print(array1)
print(array2)
#Arithmetic Operations

#Addition
print(array1+array2)

#Subtraction
print(array1 - array2)

#Multiplication
print(array1 * array2)

#Matrix Multiplication
print(array1 @ array2)

#Exponentiation
print(array1 ** 3)

#Division
print(array2 / array1)

#Mod
print(array2 % array1)

#Transpose
#converts rows into columns & columns into rows
array3 = np.array([[10,-7,0, 20],[-5,1,200,40],[30,1,-1,4]])
print(array3)

#Sorting
#By default, numpy does sorting in ascending order
array4 = np.array([1,0,2,-3,6,8,4,7])
array4.sort()
print(array4)

'''In 2-D array, sorting can be done along either of the axes i.e., row-wise or column-wise. By
default, sorting is done row-wise (i.e., on axis = 1). It means to arrange elements in each row in
ascending order. When axis=0, sorting is done column-wise, which means each column is sorted
in ascending order'''
array4 = np.array([[10,-7,0, 20],[-5,1,200,40],[30,1,-1,4]])

#default is row-wise sorting
array4.sort()
print(array4)

array5 = np.array([[10,-7,0, 20],[-5,1,200,40],[30,1,-1,4]])
array5.sort(axis=0)
print(array5)
