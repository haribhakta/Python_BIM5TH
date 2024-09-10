import matplotlib.pyplot as plt
# Data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 20, 35, 15]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
# Create a donut chart by adding a circle in the middle
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# Add a white circle in the center to create a donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
plt.title('Donut Chart')
# Display the chart
plt.show()
