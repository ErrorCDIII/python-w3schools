# Filtering Arrays

# Getting some elemnts out of an existing array and creating a new one out
# of them is callled filtering

# In NumPy, you filter an array using a boolean index list

# A boolean index list is a list of booleans corresponding to indexes in 
# the array

# If the value ar the index is True that element is contained in the 
# filtering array, otherwise it is excluded from it

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

# Note: the new array contains only the values where the filter array had
# a value True, in this case, index 0 and 2

# Creating the Filter Array

print()

import numpy as np

arr = np.array([41, 42, 43, 44])

# create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print()

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = list()
# alternative to []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Creating Filter Directly From Array

print()

import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42
# will return booleans

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Example: create a filter array that will return only even elements from
# the original

print()

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
