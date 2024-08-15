import numpy as np
# 2D array (matrix)
print("2D Array")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print("Three Dimensions")
# 3D array (tensor)
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor)
# Output:
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
darray = np.arange(24).reshape(3,2,2)
print("Three dimensions:")
print(darray)