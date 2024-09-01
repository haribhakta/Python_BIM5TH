import numpy as np
# Creating an array from 0 to 9
print("Array from 0 to 9")
array1 = np.arange(0, 10)
print(array1)
# Output: [0 1 2 3 4 5 6 7 8 9]

print("Array with step")
# Creating an array from 0 to 10 with a step of 2
array2 = np.arange(0, 10, 2)
print(array2)
# Output: [0 2 4 6 8]

print("Array with step 0.1 from 0 to 1")
# Creating a floating-point array from 0 to 1 with a step of 0.1
array3 = np.arange(0, 1, 0.1)
print(array3)
# Output: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

# Creating an array of 5 evenly spaced values from 0 to 1
array1 = np.linspace(0, 1, 5)
print("linesace",array1)
# Output: [0.   0.25 0.5  0.75 1.  ]

# Creating an array of 10 evenly spaced values from 0 to 2π
array2 = np.linspace(0, 2 * np.pi, 10)
print(array2)


# Creating an array of 5 values from 10^0 to 10^2
array1 = np.logspace(0, 2, 5)
print(array1)
# Output: [  1.  3.16227766  10.  31.6227766  100. ]

# Creating an array of 4 values from 2^1 to 2^4
array2 = np.logspace(1, 4, 4, base=2)
print(array2)
# Output: [ 2.  4.  8. 16.]

