import matplotlib.pyplot as plt
import numpy as np
# Data for grouped bar graph
categories = ['A', 'B', 'C', 'D', 'E']
values1 = [5, 7, 3, 8, 4]
values2 = [6, 4, 8, 5, 7]
# Positioning the bars
x = np.arange(len(categories))
width = 0.3  # Width of bars
# Create grouped bar graph
plt.bar(x - width/2, values1, width=width, label='Group 1', color='blue')
plt.bar(x + width/2, values2, width=width, label='Group 2', color='orange')
# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Graph')
# Add custom tick labels for x-axis
plt.xticks(x, categories)
# Add legend
plt.legend()
# Display the plot
plt.show()
