# Random Permutations

# Random Permutations of Elements

# A permutation refers to an arrangement of elements e.g. [3, 2, 1] is a 
# permutation of [1, 2, 3] and vice-versa

# The NumPy Random module provides two methods for this: shuffle() 
# and permutation()

# Shuffling Arrays

# SHuffle means changing arrangement of elements in-place i.e. in the 
# array itself

# Example: Randomly shuffle elements of the following array

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

# Note: the shuffle() metho makes changes to the original array

# Generating Permutation of Arrays

# Example: generate a random permutation of elements of the following array

print()

from numpy import random
import numpy as np
# redundancy

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(random.permutation(arr))

# Note: the permutation() method returns a re-arranged array (and leaves the
# original one unchanged)
