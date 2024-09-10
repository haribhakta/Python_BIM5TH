import matplotlib.pyplot as plt
# Data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 20, 35, 15]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
explode = (0, 0.1, 0, 0)  # "Explode" the 2nd slice (Category B)
# Create a customized pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# Add title
plt.title('Customized Pie Chart')
# Equal aspect ratio ensures the pie chart is drawn as a circle.
plt.axis('equal')
# Display the chart
plt.show()
