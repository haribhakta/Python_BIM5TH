import matplotlib.pyplot as plt
# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7]
# Create histogram
plt.hist(data, bins=5)  # Number of bins (intervals)
# Add labels and title
plt.xlabel('Data Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
# Display the plot
plt.show()
