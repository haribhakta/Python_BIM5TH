# program to find sum of numbers upto 10 th term using recursive
def sum_sequence(a, n):
    if n == 0:
        return 0
    else:
        return a + sum_sequence(a + 1, n - 1)

# Start with the first term and sum 10 terms
total_sum = sum_sequence(1, 100)
print(total_sum)
