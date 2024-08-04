import numpy as np
# Generate arrays with random values.
print("Random number from 0 to 1")
random_array = np.random.rand(3, 3)  # Uniform distribution between 0 and 1
print(random_array)
# Output:
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]
#  [0.43758721 0.891773   0.96366276]]

print("Random number from 0 to 9")
# Random integers between 0 and 9
random_int_array = np.random.randint(0, 10, (2, 3))
print(random_int_array)
# Output:
# [[3 7 1]
#  [2 9 0]]
