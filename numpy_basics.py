# array_creation Example

import numpy as np

#using list
a = np.array([2,3,4])

#print (a.dtype)

b = np.array([1.2, 3.5, 5.1])
#print (b.shape)
#print (b.dtype)

# 
b = np.array([(1.5,2,3), (4,5,6)])
#print (b)
#print (b.ndim)

# The type of the array can also be explicitly specified at 
# creation time
c = np.array( [ [1,2], [3,4] ], dtype=complex )
#print (c)

data2 = [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
arr2 = np.array(data2)

# create arrays as 0 and 1 as its elements

#print (np.zeros(10))
#print (np.ones(5))
#print ( np.ones_like(arr2))

zeros = np.zeros( (3,4) )
#print (zeros)

# How to create a boolean array?
np.full((3, 3), True, dtype=bool)
# or
np.ones((3,3), dtype=bool)

ones =  np.ones( (2,3,4), dtype=np.int16 )
#print (ones)
#print (ones.ndim)
#print (print (ones.sum(axis=0)))

emptys = np.empty( (2,3) )
#print (emptys)

# To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.
array1 = np.arange( 10, 30, 5 )
#print (array1)

float_array = np.arange( 0, 2, 0.3 )    # it accepts float arguments


x = np.arange(12).reshape((3,4))
print (x)
print (x.sum(axis=0))		# 0 = col sum; 1 = row sum


x = np.arange(12).reshape((2, 2,3))
#print (x)
#print (x.sum(axis=2))	# 0 = col sum across matrix,	1= col sum within matrix	2 = row sum with in matrix


# convert or cast an array from one type to another
arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(np.float64)
#print (float_arr.dtype)

# Convert array of strings representing numbers into numeric
numeric_strings = np.array( ['1.25', '-9.4', '46'])
#print( (numeric_strings.astype(np.float32)).astype(int) )


arr = np.arange(10)

#print( arr[5])
#print( arr[5:8])

arr[5:8] = 12
#print(arr)

arr_slice = arr[5:8]
#print (arr_slice)
arr_slice[1] = 12345
#print(arr)
arr_slice[:] = 64
#print( arr)

arr_slice = arr[5:8].copy()
arr_slice[:] = 90
#print( arr)

arr2d = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print (arr2d[2])		# [7,8,9]
#print (arr2d[0][2])	# 3
#print (arr2d[0,2])		# 3

# create 2 x 2 x 3 array
arr3d = np.array( [[[1, 2, 3],[4, 5, 6]], [[7, 8, 9], [10, 11, 12]]] )
#print (arr3d)
#print (arr3d[1][:1,1:])		# [[8,9]]

# How to extract items that satisfy a given condition from 1D array?
# Extract odd numbers
arr[arr % 2 == 1]

# How to replace items that satisfy a condition with another value in numpy array?
# Replace < 35 by 35
arr[arr < 35] = 35

# How to replace items that satisfy a condition without affecting the original array?
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)

# Convert a 1D array to a 2D array with 2 rows
arr = np.arange(10).reshape(2,-1)
#arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols

# How to get the common items between two python numpy arrays?
a1 = np.arange(10)
a2 = np.arange(5, 10)
print (np.intersect1d(a1, a2))

# How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
# From 'a' remove all of 'b'
np.setdiff1d(a,b)

# How to get the positions where elements of two arrays match?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print (np.where(a == b))

# How to extract all numbers between a given range from a numpy array?
a = np.array([2, 6, 1, 9, 10, 3, 27])
print (a[(a>= 5) & (a <= 10)])
