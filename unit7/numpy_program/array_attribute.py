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

# returns total bytes of an array
print(arr.nbytes)  # Output: 48 (for a 2x3 array with int64 elements)

# return transposed versions of array
print("Array:")
print(arr)
print("Transposed Array:")
print(arr.T)

# returns collapsed array into one dimensions
print("One dimension array")
print(arr.flatten())  # Output: [1 2 3 4 5 6]

complex_arr = np.array([1+2j, 3+4j])
print("Real part")
print(complex_arr.real)  # Output: [1. 3.]
print("Imaginary part")
print(complex_arr.imag)  # Output: [2. 4.]





