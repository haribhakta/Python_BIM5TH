# WAP in python to enter a number and find whether it is
# palindrome or not.
n = int(input("Enter a number = "))
rev = 0
x = n
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = int(n / 10)
if x == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")
