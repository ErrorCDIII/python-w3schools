# Chi Square Distribution

# Is used as a basis to verify the hypothesis

# It has two parameters:
#   df - degree of freedom
#   size - the shape of the returned array

from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)

# Visualization of Chi Square Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df=1, size=10000), kind="kde")

plt.show()
