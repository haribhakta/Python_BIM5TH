import matplotlib.pyplot as plt
# Sample data for two datasets
data1 = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6]
data2 = [3, 3, 4, 4, 4, 5, 5, 6, 7, 7]
# Overlay two histograms
plt.hist(data1, bins=5, alpha=0.5, label='Dataset 1', color='blue', edgecolor='black')
plt.hist(data2, bins=5, alpha=0.5, label='Dataset 2', color='green', edgecolor='black')
# Add labels, title, and legend
plt.xlabel('Data Values')
plt.ylabel('Frequency')
plt.title('Multiple Histograms')
plt.legend()
# Display the plot
plt.show()
