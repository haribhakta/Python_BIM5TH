import matplotlib.pyplot as plt
# Sample data with outliers
data = [7, 12, 5, 15, 6, 17, 8, 13, 9, 10, 14, 3, 2, 30, -5]
# Create a box plot showing outliers
plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='lightblue'))
# Add title and labels
plt.title('Box Plot with Outliers')
plt.ylabel('Values')
# Display the plot
plt.show()
