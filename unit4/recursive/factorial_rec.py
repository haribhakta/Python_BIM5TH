
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a positive integer: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} is {factorial(number)}")
