import numpy as np
# Creating a 2x3 array filled with the value 7
array1 = np.full((4, 3), 8)
print(array1)

zeros_array = np.zeros((3, 4))
print(zeros_array)

ones_array = np.ones((2, 3))
print(ones_array)

empty_array = np.empty((2, 2))
print(empty_array)

identity_matrix = np.eye(3)
print(identity_matrix)