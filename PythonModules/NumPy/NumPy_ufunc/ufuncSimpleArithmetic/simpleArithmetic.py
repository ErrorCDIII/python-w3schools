# Simple  Arithmetic

# Addition

# The add() function sumsthe content of two arrays, and returns the result
# as a new array

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)

# Subtraction

print()

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 23, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)

# Multiplication

# The multiply() finction multiplies the values from one array with the 
# values from another array, and return the results in a new array

print()

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

# Division

print()

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

# Power

print()

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)

# Remainder

# Both mod() and remainder() functions return the remainder of the values in 
# the first array corresponding to the values in the second array, and 
# return the results in a new array

print()

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr1 = np.mod(arr1, arr2)
newarr2 = np.remainder(arr1, arr2)

print(newarr1)
print(newarr2)

# Quotient and Mod

# The divmod() function returns both the quotient and the mod.
# The return value is two arrays, the first one contains the quotient and 
# the second one contais the mod

print()

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)

# Absolute Values

# Both absolute() and abs() functions do the same absolute operation 
# element-wise but we should use absolute() to avoid confusion with Python's 
# inbuilt math.abs()

print()

import numpy as np

arr = np.array([-1, -2, 1, 2, 3 -4])

newarr = np.absolute(arr)

print(newarr)
