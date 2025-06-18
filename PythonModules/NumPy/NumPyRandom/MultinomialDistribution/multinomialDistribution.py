# Multinomial Distribution

# Is a generalization of binomial distribution.

# Describes outcomes of multi-nomial scenarios unlike binomial where 
# scenarios must only be one of two

# It has three paramters:
#   n - number of times to run the experiment
#   pvals - list of probabilities of outcomes
#   size - the shape of the returned array

from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

# Note: multinomial samples will NOT produce single values!
# They will produce one value for each pval.

# Note: as they are a generalization of binomial distribution their visual 
# representation and similarity of normal distribution is same as that of 
# multiple binomial distributions
