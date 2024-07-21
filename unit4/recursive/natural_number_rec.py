# Example: Recursive Function to Print Numbers
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)

# Call the function with 10
print_numbers(10)