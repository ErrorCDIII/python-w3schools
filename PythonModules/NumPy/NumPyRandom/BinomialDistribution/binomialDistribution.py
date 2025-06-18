# Binomial Distribution

# Binomial Distribution is a Discrete Distribution

# It describes the outcome of binary scenarios, e.g. toss of a coin, it 
# will either be head or tails.

# It has three parameters:
#   n - number of trials
#   p - probability of occurence of each trial
#   (e.g. for toss of a coin 0.5 each coin face)
#   size - the shape of the retuned array

# Discrete Distribution
# Defined at a seperate set of events, e.f. a coin toss's result is discrete
# as it can only be head or tails wehereas the height of people is continuous
# as it can vary indiscriminately

# Example: given 10 trials for coin toss generate 10 data points

from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)

# Visualization of Binomial Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10, p=0.5, size=1000))

plt.show() 


# Difference Between Normal and Binomial Distribution

# The main difference is that normal distribution is continuous whereas 
# binomial is discrete, but if there are enough data points it will be 
# quite similar to normal distribution with certain loc and scale

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(loc=50, scale=5, size=1000),
    "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()
