# WAP in python to enter a number and find its digitsum
n = int(input("Enter a number = "))
s = 0
while n > 0:
    r = n % 10
    s = s + r
    n = int(n / 10)
print("Digit sum = ", s)

# WAP to enter a number and check whether it is palindrome or not.
# user allows to input a password up to 4 attempt.
