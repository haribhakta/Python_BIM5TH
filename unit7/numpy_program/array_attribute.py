import numpy as np
# find size of array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)

# returns number of dimensions
print(arr.ndim)  # Output: 2

# total number of array
print(arr.size)  # Output: 6

# returns size of bytes in each element
print(arr.itemsize)  # Output: 8 (for int64, this can vary)

# returns data type
print(arr.dtype)  # Output: dtype('int64') (depending on your system)