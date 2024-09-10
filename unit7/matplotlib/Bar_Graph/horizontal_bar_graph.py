import matplotlib.pyplot as plt
# Data for categories and values
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]
# Create a horizontal bar graph
plt.barh(categories, values, color='lightgreen', edgecolor='black')
# Add labels and title
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Graph')
# Display the plot
plt.show()
