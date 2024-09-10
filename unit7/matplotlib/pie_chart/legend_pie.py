import matplotlib.pyplot as plt
# Data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 20, 35, 15]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
# Create a pie chart with a legend
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart with Legend')
# Add a legend
plt.legend(labels, loc="best")
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
# Display the chart
plt.show()
