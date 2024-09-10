import matplotlib.pyplot as plt
# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7]
# Density histogram
plt.hist(data, bins=6, density=True, color='lightcoral', edgecolor='black', alpha=0.7)
# Add labels and title
plt.xlabel('Data Values')
plt.ylabel('Density')
plt.title('Density Histogram')
# Display the plot
plt.show()
