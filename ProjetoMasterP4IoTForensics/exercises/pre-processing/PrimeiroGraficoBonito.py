import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np

# primeiro_grafico_count_100_count = open("primeiro_grafico_count_100.txt","r")
# primeiro_grafico_median_100_median = open("primeiro_grafico_median_100.txt","r")

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# # create random data
# # xdata = np.random.random([2, 10])

# # split the x data into two parts
# xdata1 = primeiro_grafico_count_100_count[0, :]
# xdata2 = primeiro_grafico_count_100_count[1, :]

# # sort the x data so it makes clean curves
# xdata1.sort()
# xdata2.sort()

# # split the y data into two parts
# ydata1 = primeiro_grafico_median_100_median[0, :]
# ydata2 = primeiro_grafico_median_100_median[1, :]

# # sort the y data so it makes clean curves
# ydata1.sort()
# ydata2.sort()

# Fixing random state for reproducibility
np.random.seed(19680801)

# create random data
xdata = np.random.random([2, 10])

# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()

# create some y data points
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')

# create the events marking the x data points
xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

# create the events marking the y data points
yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                           orientation='vertical')

# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# set the limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

ax.set_title('line plot with data points')

# display the plot
plt.show()