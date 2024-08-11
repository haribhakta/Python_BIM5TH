import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Accessing array elements")
print(arr[0])  # Output: 1
print(arr[2])  # Output: 3

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Accessing element of 2D array")
print(arr[1, 1])  # Output: 5

print("Accessing entire row")
print(arr[0])    # Output: [1, 2, 3]  (first row)
print("Accessing entire column")
print(arr[:, 1]) # Output: [2, 5, 8]  (second column)

arr = np.array([1, 2, 3, 4, 5])

print("Element from 1 to 3",arr[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)
print("First three Element",arr[:3])   # Output: [1, 2, 3] (first three elements)
print("Every second element",arr[::2])  # Output: [1, 3, 5] (every second element)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Rows from 1 to end cols from 0 to 1",arr[1:, :2])

arr = np.array([1, 2, 3, 4, 5])
print("Element > 3",arr[arr > 3])  # Output: [4, 5] (elements greater than 3)
