# Products

# To find the products of the elements in an array, use the prod() function

# Example: find the products of the elements of this array
import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)

print()

# Example: find the produt of the elements of two arrays

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)

# Product Over an Axis

# If you specify axis=1, Numpy will return the product of each array

# Example: perform summation in the following array over 1st axis

print()

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)

# Cummulative Product

# Cummulative productmeans taking the product partially

# Perform partial sum with the cumprod() function

# Example: take cummulative product of all elements for following array

print()

import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)
