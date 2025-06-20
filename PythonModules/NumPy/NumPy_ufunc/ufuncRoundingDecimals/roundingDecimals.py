# Rounding Decimals

# There are primarily five ways of rouding off decimals in NumPy:
#   truncation
#   fix
#   rouding
#   floor
#   ceil

# Truncation

# Remove the decimals, and return the float number closest to zero.
# Use the trunc() and fix() functions

# Example: truncate elements of the following array
import numpy as np

arr1 = np.trunc([-3.1666, 3.6667])
arr2 = np.fix([-3.1666, 3.6667])

print(arr1)
print(arr2)

# Rounding

# The round() function increments digit or decimal by 1 if >= 5 else do 
# nothing

# Example: round off 3.1666 to 2 decimal places
import numpy as np

arr = np.round(3.1666, 2)

print()

print(arr)

# Floor

# The floor() function rounds off decimal to the nearest lower integer

# Example: floor the elements of the following array

print()

import numpy as np

arr = np.floor([-3.1666, 3.667])

print(arr)

# Ceil

# The ceil() function rounds off decimals to the nearest upper integer

# Example: ceil the elements of the following array
print()

import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr)
