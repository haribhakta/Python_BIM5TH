def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter a positive integer: "))
if number < 0:
    print("Fibonacci sequence is not defined for negative numbers.")
else:
    for i in range(0,number):
        print(fibonacci(i))
