# Data Types

# Data Types in NumPy

# Besides the regular Python data types NumPy has some extra data 
# types, and refer to data types with one character

# NumPy Data Types
#   i - integer
#   b - boolean
#   u - unsigned integer
#   f - float
#   c - complex float
#   m - timedelta
#   M   - datetime
#   O - object
#   S - string
#   U - unicode string
#   V - fixed chunck of memory for other type (void)

# Checking the Data Type of an Array

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

# Creating Arrays With a Defined Data Type

# We use the array() function to create arrays, this function can 
# take an optional argument: dtype that allows us to define the 
# expected data type of the array elements

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print()

print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print()

print(arr)
print(arr.dtype)

# What if a Value Can Not Be Converted?

# If a type is given in which elements can't be casted then NumPY
# will raise a ValueError

import numpy as np

# arr = np.array(['a', '2', '3'], dtype='i')
# This will raise an arror since a cannot be cast as an integer

# Converting Data Type on Existing Arrays

# Thes bets way to change the data type of an existing array, it to 
# make a copy of it with the astype() method

# The astype() method creates a copy of the array and allows you to
# specify the data type as a parameter

# The data type can be specified using a string
#   f - float
#   i - integer

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print()

print(newarr)
print(newarr.dtype)

print()

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

print()

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print()

print(newarr)
print(newarr.dtype)
