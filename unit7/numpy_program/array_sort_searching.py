import numpy as np

arr = np.array([300, 100, 200])
sorted_arr = np.sort(arr)
print(sorted_arr)  # Output: [100 200 300]

arr = np.array([300, 100, 200])
indices = np.argsort(arr)
print(indices)  # Output: [1 2 0]

names = np.array(['Alice', 'Nob', 'Charlie'])
ages = np.array([25, 30, 20])
indices = np.lexsort((names, ages))
print("Lex Sort : ",indices)

# searching
arr = np.array([10, 20, 30, 40, 50])
indices = np.where(arr > 30)
print("Where Condition = ",indices)  # Output: (array([3, 4]),)

arr = np.array([1, 3, 5, 7])
indices = np.searchsorted(arr, 4)
print(indices)  # Output: 2

arr = np.array([0, 1, 0, 2, 3])
indices = np.nonzero(arr)
print(indices)  # Output: (array([1, 3, 4]),)





