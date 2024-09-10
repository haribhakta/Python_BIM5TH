import matplotlib.pyplot as plt
# Data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 20, 35, 15]
# Create a basic pie chart
plt.pie(sizes, labels=labels)
# Add title
plt.title('Basic Pie Chart')
# Display the chart
plt.show()
