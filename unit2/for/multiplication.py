# WAP to enter a number and print its multiplication table
n=int(input("Enter a number = "))
print("Multiplication Table of ",n)
for i in range(1,11):
    m=n*i
    print(n,"X", i, " = ",m )
