import matplotlib.pyplot as plt
# Sample data
data1 = [7, 12, 5, 15, 6, 17, 8, 13, 9, 10, 14, 3, 2]
data2 = [5, 8, 12, 14, 7, 10, 16, 11, 18, 9, 13, 6, 4]
# Combine the data into a list
data = [data1, data2]
# Create box plots for multiple datasets
plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
# Add title and labels
plt.title('Multiple Box Plots')
plt.xticks([1, 2], ['Dataset 1', 'Dataset 2'])
plt.ylabel('Values')
# Display the plot
plt.show()
