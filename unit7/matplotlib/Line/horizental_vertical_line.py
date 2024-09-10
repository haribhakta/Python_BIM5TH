import matplotlib.pyplot as plt

# Create a plot
plt.plot([1, 2, 3], [1, 4, 9], label='Line')

# Add a horizontal line at y=2
plt.axhline(y=2, color='r', linestyle='--', label='Horizontal Line')

# Add a vertical line at x=2
plt.axvline(x=2, color='g', linestyle=':', label='Vertical Line')

# Show legend
plt.legend()

# Show the plot
plt.show()
