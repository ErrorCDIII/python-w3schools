# What's a Random Number?

# Random number does NOT mean a different number every time.
# Random means something that can not be predicted logically

# Pseudo Random and True Random

# Random numbers generated through a generation algorithm are called pseudo
# random and are not truly random

# In order to generate a truly random number we need to get the random data
# from outside sources.
# The outside source is generally our keystrokes, mouse movements, data on
# network, etc

# Generate Random Number

# NumPy offers the random module to work with random numbers

from numpy import random

x = random.randint(100)

print(x)

print()

acc = 10
while acc > 0:
    print(random.randint(100))
    acc -= 1

# Generate Random Float

# The random module's rand() method returns a random float between 0 and 1

print()

from numpy import random

x = random.rand()

print(x)

# Generate Random Array

# In Numpy we work with arrays, and you can use the two methods from the 
# above examples to make random arrays

# Integers

# The randint() method takes a size parameter where tou can specify the 
# shape of an array

print()

from numpy import random

x = random.randint(100, size=5)

print(x)

# Example: generate a 2-D array with 3 rows, each row containing 5 random
# integers from 100 to 100

print()

from numpy import random

x = random.randint(100, size=(3, 5))

print(x)

# Floats

# The rand() method also allows you to specify the shape of the array

# Example: genrate a 1-D array containing 5 random floats

print()

from numpy import random

x = random.rand(5)

print(x)

# Example: generate a 2-D array with 3 rows, each row containing 5 random 
# numbers

print()

from numpy import random

x = random.rand(3, 5)

print(x)

# Generate Random Number From Array

# The choice() method allows you to generate a random vlaue based on an 
# array of values

# The choice() method takes an array as a parameter and randomly returns
# one of the values

# Example: return one of the values in an array

print()

from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)

# The choice() method also allows you to return an array of values
# Add a size parameter to specify the shape of the array

print()

from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))
