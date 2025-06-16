# Sorting Arrays

# The NumPy ndarray object has a function called sort(), that 
# will sort a specified array

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# Note: this method returns a copy of the array, leaving the 
# original unchanged

# You can also sort arrays of strings, or any other data type

import numpy as np

arrStrings = np.array(['baba', 'cherry', 'apple'])

arrBools = np.array([True, False, True])

print()

print(np.sort(arrStrings))

print()

print(np.sort(arrBools))

# Sorting a 2-D Array