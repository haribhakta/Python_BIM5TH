# WAP in python to enter a number and find whether it is
# armstrong or not.
n = int(input("Enter a number = "))
s = 0
x = n
while n > 0:
    r = n % 10
    s = s + r * r * r
    n = int(n / 10)
if x == s:
    print("It is armstrong")
else:
    print("It is not not armstrong")
