# Searching Arrays

# You can search an array for a certain value, and return the 
# indexes that get a metch

# To search an array, use the where() method

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
# Note: the example above will result in a tuple

# Even values

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print()

print(x)

# Odd values

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print()

print(x)

# Search Sorted

# There is a method called searchsorted() which performs a binary 
# search in the array, and returns the index where the specified 
# value would be inserted to maintain the search order

# The searchorder() method is assumed to be used on serted arrays

# Example: find the indexes where the value 7 should be inserted

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print()

print(x)

# Search From the Right Side

# By default the left most index is returned, but we can give 
# side='right' to return by the right most index instead

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print()

print(x)

# Multiple Values

# To search for more than one value, use an array with the specified values

import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print()

print(x)
