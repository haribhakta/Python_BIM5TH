import matplotlib.pyplot as plt
# Sample data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Create a line plot
plt.plot(x, y, label="This is Line plot")

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line in Matplotlib')

# Show legend
plt.legend()

# Show the plot
plt.show()
