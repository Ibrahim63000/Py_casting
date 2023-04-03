"""
File to plot radar image with matplotlib and cartopy
"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

#let's create some data and play with it
rand_data=np.random.uniform(low=0.5, high=10, size=(100,100))

print(rand_data)
plt.plot(rand_data)
plt.show()
