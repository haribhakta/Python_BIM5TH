# WAP to enter a number and print whether it is prime or composite
# WAP to print all prime number up to 100.
n = int(input("Enter a number = "))
c = 0
for i in range(2,n):
    if n % i == 0:
        c = c+1
        break
if c == 0:
    print(n, "is prime")
else:
    print(n, "is composite")
