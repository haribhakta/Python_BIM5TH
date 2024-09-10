import matplotlib.pyplot as plt
# Sample data
data = [7, 12, 5, 15, 6, 17, 8, 13, 9, 10, 14, 3, 2]
# Horizontal box plot
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightcoral'))
# Add title and labels
plt.title('Horizontal Box Plot')
plt.xlabel('Values')
# Display the plot
plt.show()
