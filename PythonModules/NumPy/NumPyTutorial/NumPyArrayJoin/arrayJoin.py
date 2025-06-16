# Joining Arrays

# We pass a sequence of arrays that we want to join to the 
# concatenate() function, along with the axis.
# If the axis is not explicitly passed, it is taken as 0 by default

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr1)
print()
print(arr2)
print()
print(arr)

# Example: join two 2-D arrays along rows (axis = 1)
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print()

print(arr1)

print()

print(arr2)

print()

print(arr)

# Joining Arrays Using Stack Functions

# Stacking is the same as concatenation, the only difference is that
# stacking is done along a new axis

# We can concatenate two 1-D arrays along the second axis which 
# would result in putting them one over the other

# We pass a sequence of arrays that we want to join to the stack()
# method along with the axis
# If the axis is not explicitly passed it is taken as 0 by default

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print()

print(arr1)

print()

print(arr2)

print()

print(arr)

# Stacking Along Rows

# NumPy provides a helper function: hstack() to stack along rows

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print()

print(arr1)

print()

print(arr2)

print()

print(arr)

# Stacking Along Comumns

# NumPy provides a helper function: vstack() to stack along collumns

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print()

print(arr1)

print()

print(arr2)

print()

print(arr)

# Stacking Along Height (depth) 

# NumPy provides a helper fucntion: dstack() to stack along height,
# which is the same as depth

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print()

print(arr)
