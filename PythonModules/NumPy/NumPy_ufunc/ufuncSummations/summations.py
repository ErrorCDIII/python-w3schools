# Summations

# What's the difference between summation and addition?

# Addition is done between two arguments whereas summation happens over n 
# elements

# Example: add the values in arr1 to the values in arr2

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)
# returns: [2 4 6]

print()

# Example: sum the values in arr1 and the values in arr2

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)
# returns 12

# Summation Over an Axis

# If you specify axis=1, NumPy will sum the numbers in each array

# Example: perform summation in the following array over 1st axis

print()

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)
# returns [6 6]

# Cummulative Sum

# Means partially adding the elements in an array

# Perform partial sum with the cumsum() function

# Example: perform cummulative summation in the following array

print()

import numpy as np

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)
# returns [1 3 6]
