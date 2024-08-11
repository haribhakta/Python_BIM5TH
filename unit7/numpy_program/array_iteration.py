import numpy as np

# 2D array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Using For")
for row in arr:
    print(row)

print("Using nditer")
for element in np.nditer(arr):
    print(element)

print("using ndindex")
for index in np.ndindex(arr.shape):
    print(f"Index: {index}, Value: {arr[index]}")

def my_function(x):
    return x.sum()

# Apply function along each row (axis=1)
result = np.apply_along_axis(my_function, axis=1, arr=arr)
print(result)


