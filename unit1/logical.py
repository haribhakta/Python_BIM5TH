# WAP to find the greatest among three numbers
a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))
if (a>b and a>c):
    print("The greatest = ",a)
elif (b>c):
    print("The greatest = ",b)
else:
    print("The greatest = ",c)
