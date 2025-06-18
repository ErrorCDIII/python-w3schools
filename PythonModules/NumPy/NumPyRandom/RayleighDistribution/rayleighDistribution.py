# Rayleigh Distribution

# Is used for signal processing

# It has two parameters:
#   scale - standard deviation - decides how flat the distribution will be
        # - default is 1.0
#   size - the shape of the returned array

from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

# Visualization of Rayleigh Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()

# Similarity Between Rayleigh and Chi Square Distribution

# At unit stddev and 2 degrees of freedom rayleigh and chi square 
# represent the same distributions
