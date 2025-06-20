# Differences

# A discrete difference means subtracting two successive elements

# To find the discrete difference, use the diff() function

# Example: compute the discrete difference of the following array

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr) 

# We can perform this operation repeatedly by giving parameter n

# Example: compute discrete difference of the following array twice

print()

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)
