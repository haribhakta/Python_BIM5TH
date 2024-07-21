# A lambda function that adds 10 to the input
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

# Using lambda function to square elements in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Using lambda function to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Sorting a list of tuples based on the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
