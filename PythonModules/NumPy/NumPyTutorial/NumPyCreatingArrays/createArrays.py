# Create a NumPy ndarray Object

# NumPy is used to work with arrays.
# The array object in NumPy os called ndarray

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

# To create an ndarray, we can pass a list, a tuple or an array-like
# # object into the array() method, and it will be converted int
# # an ndarray

import numpy as np

print()

arr = np.array((1, 2, 3, 4, 5))

print(arr)

# Dimensions in Arrays

# A dimension in arrays is one level of array depth (nestesd arrays)
# Nested arrays are arrays that arrays as their elements

# 0-D Arrays

# Or Scalars, are the elements in an array.
# Each value in an array is a 0-D array

# Example: create a 0-D array with value 42

import numpy as np

print()

arr = np.array(42)

print(arr)

# 1-D Arrays

# An that array has 0-D arrays as it's elements is called 
# uni-dimenstional or 1-D array.
# These are the most common and basic arrays

# Example: create a 1-D array containing the values 1,2,3,4,5

import numpy as np

print()

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# 2-D Arrays

# An array that has 1-D arrays as it's elements is called a 2-D array

# These are often used to represent matrix or 2nd order tensors

# NumPy has a sub module dedicated to matrix operations called
# numpy.mat

# Example: create a 2-D array containing two arrays with the
# values 1,2,3 and 4,5,6

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print()

print(arr)

# 3-D Arrays

# An array that has 2-D arrays (matrices) as it's elements

# These are often used to represent 3rd order tensors

import numpy as np

print()

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

# CHeck Number of Dimensions

# NumPy Arrays provide the ndim attribute that returns an interger
# that tells us how many dimensions the array have

import numpy as np

print()

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays

# An array can have any number of dimensions

# When an array is created, you can define the number of dimensions
# by using the ndim argument

import numpy as np

print()

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :' , arr.ndim)
