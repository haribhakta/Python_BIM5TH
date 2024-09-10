import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6], color='red')
# plt.plot([1, 2, 3], [4, 5, 6], color=(0.2, 0.4, 0.6))  # RGB color
# plt.plot([1, 2, 3], [4, 5, 6], color='#FF5733')  # Hex color
plt.show()

import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
plt.scatter(x, y, c=colors, cmap='viridis')  # Using a colormap
plt.colorbar()  # Add colorbar for reference
plt.show()


