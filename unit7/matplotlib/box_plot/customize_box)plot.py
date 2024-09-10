import matplotlib.pyplot as plt
# Sample data
data = [7, 12, 5, 15, 6, 17, 8, 13, 9, 10, 14, 3, 2]
# Customize the box plot
plt.boxplot(data, notch=True, patch_artist=True, boxprops=dict(facecolor='lightblue'))
# Add title and labels
plt.title('Customized Box Plot')
plt.ylabel('Values')
# Display the plot
plt.show()
