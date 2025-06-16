# Array Copy vs View

# The copy creates a new array and the view does not

# The changes to a view change the original array

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# Note: the copy SHOULD NOT be affected by the changes made to the 
# original array

# View

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print()

print(arr)
print(x)

# Note: the view SHOULD be affected by the changes to the original array

# Make Changes in the View

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print()

print(arr)
print(x)

# Note: the original SHOULD be affected by the changes made to the view

# Check if Array Owns it's Data

# Every NumPy array has the attribute base and returns None if the 
# array owns the data.
# Otherwise, the base attribute refers to the original object

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print()

print(x.base)
print(y.base)
# Note: the copy returns None
# Note: the view returns the original array
