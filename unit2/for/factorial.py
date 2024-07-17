# WAP to enter a number and find its factorial value
n=int(input("Enter a number = "))
f=1
for i in range(1,n+1,1):
    f=f*i
print("Factorial value = ",f)
