# WAP to enter marks in five subjects and find out percentage and 
# grade.
print("Enter marks of five subjects:")
s1=float(input("Enter marks in Python = "))
s2=float(input("Enter marks in Java = "))
s3=float(input("Enter marks in C = "))
s4=float(input("Enter marks in Web = "))
s5=float(input("Enter marks in Math = "))
t=s1+s2+s3+s4+s5
print("Total Marks = ",t)
p=t/5
print("Percent= ",p)
if(p>=90):
    g="A+"
elif (p>=80):
    g="A"
elif (p>=70):
    g="B+"
elif (p>=60):
    g="B"
elif (p>=50):
    g="C+"
elif (p>=40):
    g="C"
else:
    g="NG"
print("Grade = ",g)

# Lab Exp 2 Conditional Satement in Python
# 1. WAP to enter item name, quantity, rate of an item and 
# print total amount, discount, and net amount after VAT 13%.
# the discount is given below.
# if amount>=10000,2%,amount >=20000,3%,amount>=50000,5% and 
# above 100000, 10%
