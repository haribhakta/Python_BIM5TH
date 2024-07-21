# To print the sequence 5, 10, 15, 20 upto 10th term using a recursive function in Python, you can define a function that prints numbers in increments of 5, starting from 5 and ending at 20. Here's how you can do it:
def print_sequence(a, n):
    if n > 0:
        print(a)
        # Call the function recursively with the next term and one less term to print
        print_sequence(a + 5, n - 1)

# Start with the first term and print 10 terms
print_sequence(5, 10)
