import numpy as np

print("Random number from 0 to 1")
random_array = np.random.rand(3, 3)  # Uniform distribution between 0 and 1
print(random_array)

print("Random number from 0 to 9")
random_int_array = np.random.randint(100, 999, (3, 4))
print(random_int_array)

print("Specified value initialization array")
array1 = np.full((2, 3), 7)
print(array1)

print("Zero array")
zeros_array = np.zeros((3, 4))
print(zeros_array)

print("Ones array")
ones_array = np.ones((2, 3))
print(ones_array)

print("Empty array")
empty_array = np.empty((2, 2))
print(empty_array)

print("Identity matrix")
identity_matrix = np.eye(3)
print(identity_matrix)

