# Logs

# NumPy provides functions to perform log at base 2, e and 10

# We will explore how we can take log for any base by creating a custom ufunc

# All of the log functions will place -inf or inf in the elements if the log 
# can not be computed

# Log at Base 2

# Use the log2() function to perform log at base 2

# Example: find log at base 2 of all elements of the following array

import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

# Note: the arrange(1, 10) function returns an array with integers starting 
# from 1 (included) to 10 (not included)

# Log at Base 10

# Use the log10() function to perform log at base 10

# Example: find log at base 10 of all elements of the following array:

print()

import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))

# Natural Log, or Log at Base e

# Use the log() function to perform log at base e

# Example: find log at base e of all elements of the following array:

print()

import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))

# Log at Any Base

# Numpy does not provide any function to take log at any base, so we can use 
# the frompyfunc() function along with inbuilt math.log() with two input 
# parameters and one output parameter

# Example

print()

from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))
