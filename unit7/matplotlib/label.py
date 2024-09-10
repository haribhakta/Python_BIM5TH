import matplotlib.pyplot as plt
# Example data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
# Plotting
plt.plot(x, y,label="This is legend")
# Adding axis labels
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('My Plot Title')
plt.legend()
plt.text(2, 25, 'Annotation at (2,25)')
plt.show()
