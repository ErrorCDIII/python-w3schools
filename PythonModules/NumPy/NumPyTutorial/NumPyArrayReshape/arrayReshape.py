# Reshaping Arrays

# Reshape Form 1-D to 2-D
 
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

# Reshape From 1-D to 3-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print()

print(newarr)

# Can We Reshape Into any Shape?

# Yes, as long as the elements required for reshaping are equal in 
# both shapes

# Note: we can reshape an 8 elements 1D array into 4 elements in 2 
# rows 2D array but we cannot reshape it into a 3 elements 3 rows 
# 2D array as that would require 3x3 = 9 elements

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(3, 3)

# print()

# print(newarr)

# This will raise an error since the number does not match

# Returns Copy or View?

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print()

print(arr.reshape(2, 4).base)
# Note: the example above returns the original array, so it's a view

# Unknown Dimension

# You are allowed to have one "unknown" dimension
# Meaning that you do not have to specify an exact number for one
# of the dimensions in the reshape method

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print()

print(newarr)
# Note: we can't pass -1 to more than one dimension

# Flattening the Arrays

# Flattening an array means converting a multidimensional array
# into a 1D arry

# We can use the reshape(-1) to achieve this

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print()

print(newarr)
# Note: there are a lot of functions for changing the shapes of 
# arrays in numpy: flatten, ravel and also rearranging the elements
# rot90, flip, flipr, flipud etc. There fall under Intermediate
# Advanced section on numpy
