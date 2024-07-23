# # Example: Recursive Function to Print Numbers
# def print_numbers(n):
#     if n > 0:
#         print_numbers(n - 1)
#         print(n)
#
# # Call the function with 10
# print_numbers(10)

# Example: Recursive Function to Print sum of  Numbers
def print_numbers(n):
    if n == 0:
        return 1
    else:
        return n + print_numbers(n-1)

# Call the function with 10
print(print_numbers(10))