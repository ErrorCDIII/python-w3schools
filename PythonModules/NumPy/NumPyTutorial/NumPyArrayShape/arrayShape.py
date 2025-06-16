# Array Shape

# The shape of an array is the number of elements in each dimension

# NumPy arrays have an attribute called shape that returns a tuple
# with each index

import numpy as np

arr =np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

# Example: create an array with 5 dimensions suing ndmin using a 
# vector with values 1,2,3,4 and verify that the last dimension
# has value 4
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print()

print(arr)
print('shape of array:', arr.shape)
