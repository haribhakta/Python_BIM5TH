import matplotlib.pyplot as plt
# Create a figure and subplots (nrows x ncols)
fig, axes = plt.subplots(nrows=2, ncols=2)  # 2x2 grid of subplots
# Access individual subplots using the axes array
axes[0, 0].plot([1, 2, 3], [4, 5, 6])  # Top-left
axes[0, 1].plot([1, 2, 3], [6, 5, 4])  # Top-right
axes[1, 0].plot([1, 2, 3], [2, 3, 4])  # Bottom-left
axes[1, 1].plot([1, 2, 3], [4, 2, 1])  # Bottom-right
# Add titles to the subplots
axes[0, 0].set_title('Plot 1')
axes[0, 1].set_title('Plot 2')
axes[1, 0].set_title('Plot 3')
axes[1, 1].set_title('Plot 4')
# Adjust the layout to prevent overlapping
plt.tight_layout()
# Show the figure
plt.show()
