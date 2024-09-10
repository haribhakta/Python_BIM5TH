import matplotlib.pyplot as plt
# Data for x and y axes
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 100, 200, 300]  # Size of markers
colors = [10, 20, 30, 40, 50]    # Color values
# Create a scatter plot with custom size and color
plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7)
# Add colorbar for the colormap
plt.colorbar(label='Color Intensity')
# Add labels and title
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Customized Scatter Plot')
# Display the plot
plt.show()
