import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
# Enable grid
# plt.grid(True)
# plt.grid(True, color='red', linestyle='--', linewidth=0.5)
plt.grid(True, axis='x')
plt.show()

