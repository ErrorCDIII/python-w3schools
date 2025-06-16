# Splitting NumPy Arrays

# We use array_split() for splitting arrays, pass it the array we 
# want to split and the number of splits

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
# Note: the return value is a list containing three arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print()

print(newarr)
# Note: we also have the method split() available but it will not
# adjust the elements when elements are less in source array for
# splitting like in the example above
# array_split() worlked properly bit split() would fail

# Split Into Arrays

# The return value of the array_split() method is an array
# containing each of the splits as an array

# If you split an array into 3 arrays, you can access from the 
# result just like any array element

# Example: access the splitted arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print()

print(newarr[0])
print(newarr[1])
print(newarr[2])

# Splitting 2-D Arrays

# Use the array_split() method, pass in the array you want to split
# and the number of splits you want to do

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.split(arr, 3)

print()

print(newarr)
# The example above returns three 2-D arrays

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print()

print(newarr)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print()

print(newarr) 

# An alternate solution is using hsplit() opposite to hstack()

# Example: use the split() method to split the 2-D array into three 
# 2-D arrays along collumns

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print()

print(newarr)
# Note: similar alternatives to vstack() and dstack() are available
# as vsplit() and dsplit()
