# Exponential Distribution

# Is used used for describing time till event

# It has two parameters:
#   scale - inverse of rate (lam in poisson distribution) - defaults to 1.0
#   size - the shape of the returned array

from numpy import random

x = random.exponential(scale=2, size=(2, 3))

print(x)

# Visualization of Exponencial Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.exponential(size=1000), kind="kde")

plt.show() 

# Relatioon Between Poisson and Exponencial Distribution

# Poisson distribution deals with number of occurences of an event in a 
# time period whereas exponential distribution deals with the time between 
# these events
