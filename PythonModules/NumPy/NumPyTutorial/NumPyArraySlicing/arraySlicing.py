# Array Slicing

# Slicing in Python means taking elements from one given index to 
# another given index

# We pass slice instead of index like this [start:end]

# We can also define the step, like this [start:end:step]

# If we don't pass start it's considered 0

# If we don't pass end it's considered the length of the array in 
# that dimension

# If we don't pass the step it's considered 1

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
# Note: as usual, the result includes the start index and excludes
# the end index

print(arr[:4]) 

# Negative Slicing

# Use minus operator (-) to refer to an index from the end

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print()

print(arr[-3:-1])

# Step

# Use the step value to determine the step of the slicing

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print()

print(arr[1:5:2])
print(arr[::2])

# Slicing 2-D Arrays

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print()

print(arr[1, 1:4])

print(arr[0:2, 2])

print(arr[0:2, 1:4])
