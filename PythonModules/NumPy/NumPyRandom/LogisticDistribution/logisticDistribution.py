# Logistic Distribution

# It's used to describe growth.

# Used in machine larning, logistic regression, neural networks, etc.

# It has three parameters:
#   loc - mean, where the peak is by default 0
#   scale - standard deviation, the flatness of the distribution - by default 1
#   size - the shape of the returned array

# Example: draw 2x3 samples from a logistic distribution with mean at 1 and 
# stddev 2.0

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

# Visualization of Logistic Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.logistic(size=1000), kind="kde")

plt.show()

# Difference Between Logistic and Normal Distribution

# Both are near identical, but logistic distribution has more area under the 
# tails, meaning it represents more possibility of occurence of an event 
# further away from mean.

# For higher value of scale (standard deviation) the normal and logistic 
# distributions are near identical apart from the peak

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(scale=2, size=1000),
    "logistic": random.logistic(size=1000)
}

sns.displot(data, kind="kde")

plt.show()
