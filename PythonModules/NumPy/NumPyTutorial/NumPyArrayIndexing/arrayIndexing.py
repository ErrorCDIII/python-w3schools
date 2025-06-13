# Access Array Elements

# Array indexing is the same as accessing an array element

# You can access an array element be referring to it's index number

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])

# Access 2-D Arrays

# To access elements from 2-D arrays we can use comma seperated 
# integers representing the dimension ad the index of the element

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print()

print('2nd element on 1st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])

# Access 3-D Arrays

# Done in a similar fashion as 2-D arrays

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print()

print(arr[0, 1, 2])

# Negative Indexing

# 3 Use negative indexing to access an array from the end

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print()

print('Last elemento from 2nd dim:', arr[1, -1])
