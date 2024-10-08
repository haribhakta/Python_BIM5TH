import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr_copy = arr.copy()

arr_copy[0] = 99

print("Original Array:", arr)   # Output: [1, 2, 3, 4, 5]
print("Copied Array:", arr_copy)  # Output: [99, 2, 3, 4, 5]

# array view
arr = np.array([1, 2, 3, 4, 5])
arr_view = arr.view()

arr_view[0] = 99
arr[1]=100
print("Original Array:", arr)   # Output: [99, 2, 3, 4, 5]
print("View Array:", arr_view)  # Output: [99, 2, 3, 4, 5]


# check array is view or copy
arr = np.array([1, 2, 3, 4, 5])
arr1 = arr.view()
arr2 = arr.copy()


print(arr1.base is arr)  # Output: True (arr_view is a view)
print(arr2.base is arr)  # Output: False (arr_copy is a copy)

