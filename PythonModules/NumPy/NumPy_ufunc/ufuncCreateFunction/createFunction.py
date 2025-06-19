# How To Create Your Own ufunc

# To create tou own ufunc, you have to define a function, like you do with
# normal functions in Python, then you add it to your NumPy ufunc library 
# with the frompyfun() method

# The frompyfunc() method takes the following arguments:
#   1. function - the name of the function
#   2. inputs - the number of input arguments (arrays)
#   3. outputs - the number of output arrays

# Example: create your own ufunc for addition:
import numpy as np

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# Check if a Function is a ufunc

# A ufunc should return the type <class 'numpy.ufunc'>

print()

import numpy as np

print(type(np.add))

# If it's not a ufunc, it will return another type

print()

import numpy as np

print(type(np.concatenate))

# Example: use the if statement to check if the function is a ufunc ot not

print()

import numpy as np

if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')
