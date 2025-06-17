# Normal Distribution

# Use the random.normal() method to get a Normal Data Distribution
# It has three parameters:
#   loc - (Mean) where the peak of the bell exists
#   scale - (Standard Deviation) how flat the graph distribution should be
#   size - the shape of the returned arrau

from numpy import random

x = random.normal(size=(2, 3))

print(x)

print()

# Example: generate a random normal distribution of size 2x3 with mean at 1 
# and standrd deviationof 2:

print()

from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

# Visualization of Normal Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()
