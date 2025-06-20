# Finding the Lowest Common Multiple

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

# Finding LCM in Arrays

# To find the LCM of all values in an array, you can use the reduce() method

# The reduce() method will use the ufunc, in this case the lcm() function, 
# on each element, and reduce the array by one dimension

# Example: find the LCM of the values of the following array

print()

import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

# Example: find the LCM of all values of an array where the array contains 
# all integers from 1 to 10

print()

import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)
