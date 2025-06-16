# Array Iterating

# Iterating on the elements of a 1-D array

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

# Iterating 2-D Arrays

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print()

for x in arr:
    print(x)
# Note: if we iterate on a n-D array it will go through the n-1th 
# dimension, one by one

# To return the actual values, the scalars, we have to iterate the
# arrays in each dimension

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print()

for x in arr:
  for y in x:
    print(y) 

# Iterating 3-D Arrays
# In a 3-D array it will go through all the 2-D arrays

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print()

for x in arr:
   print(x)

# To return the actual values, we have to iterate the arrays in 
# each dimension

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print()

for x in arr:
   for y in x:
      for z in y:
            print(x)

# Iterating Arrays Using nditer()

# The function nditer() is a helping function that can be used from
# very basic to very advanced iterarions.
# It solves somne bacic issues which we face in iteration

# Iterating on Each Scalar Element

# In basic for loops, iterating through each scalar of an array we
# need to n for loops which can be difficult to write for arrays
# with very high dimensionality

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
   print(x)

# Iterating Array With Different Data Types

# We can use op_dtypes argument and pass it the expeected datatype
# to change the datatype of the elements while iterating

# NumPy does not change the data type of the element in-place so it
# needs some other space to perfmor this action.
# That extra space is called buffer, and in order to enable it in
# nditer() we pass flags=['buffered']

import numpy as np

arr = np.array([1, 2, 3])

print()

for n in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
   print(x)

# Iterating With Different Setp Size

# We can use filtering

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print()

for x in np.nditer(arr[:, ::2]):
   print(x)

# Enumarated Iteration Using ndenumerate()

# Enumeration mens mentioning sequence number of somethings one by one

# Sometimes we requires corresponding index of the element while 
# iterating, the ndenumerate() method can be used for those usecases

# Example: 1-D arrays

import numpy as np

arr = np.array([1, 2, 3])

print()

for idx in np.ndenumerate(arr):
   print(idx, x)

# Example: 2-D arrays

import numpy as np

print()

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
   print(idx, x)
