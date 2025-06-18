# Pareto Distribution

# Follows the Paretto's law - 80-20 distribution
# 20% of the factors cause 80% of the outcome

# It has two parameters:
#   a - shape parameter
#   size - the shape of the returned array

# Example: draw out a sample for pareto distribution with shape of 2 with 
# size 2x3

from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)

# Visualization of Pareto Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))

plt.show()
