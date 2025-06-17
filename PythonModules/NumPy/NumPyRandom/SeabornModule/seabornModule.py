# Seaborn

# Visualize Distributions With Seaborn

# Seaborn is a library that uses Matplotlib underneath to plot graphs.
# It will be used to visualize random distributions

# Install Seaborn
# pip install seaborn

# Displots

# Displot stands for distribution plot, it takes as input an array and plots 
# a curve corresponding to the distribution of points in the array

# Import Matplotlib

# Import the pyplot object of the Matploitlib module in your code using
# the following statement

# import matplotlib.pyplot as plt

# Import Seaborn

# import seaborn as sns

# Plotting a Sisplot

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

# Plotting a Displot Without a Histogram

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()

# Note: we will be using: sns.displot(arr, kind="kde") to visualize random 
# distributions in this tutorial
