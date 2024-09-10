import matplotlib.pyplot as plt
# Data for categories and values
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]
# Create a basic bar graph
plt.bar(categories, values)
# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Graph')
# Display the plot
plt.show()
