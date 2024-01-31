
import matplotlib.pyplot as plt
import numpy as np
import csv
plt.rcParams['font.size'] = 28

# Example data (replace with your data)
categories = ['0', '4', '8', '12']
medians = [169, 184, 356, 548]  # Replace with your median values
std_devs = [9, 43, 104, 20]  # Replace with your standard deviation values

# Create a bar graph with error bars
fig, ax = plt.subplots()

# Plot bars
bars = ax.bar(categories, medians, yerr=std_devs, capsize=5, color='skyblue', alpha=0.7)

# Add labels and title
ax.set_ylabel('Total de blocos criados na blockchain')
ax.set_xlabel('Tempo total (seg)')

# Add legend
ax.legend(['Median'])
plt.grid(True)

# Show the plot
plt.show()