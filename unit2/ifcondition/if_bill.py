# Lab Exp 2 Conditional Satement in Python
# 1. WAP to enter item name, quantity, rate of an item and 
# print total amount, discount, and net amount after VAT 13%.
# the discount is given below.
# if amount>=10000,2%,amount >=20000,3%,amount>=50000,5% and 
# above 100000, 10%
item=input("Enter Item Name = ")
qty=int(input("Enter quantity = "))
rate=float(input("Enter rate = "))
amt=qty*rate
print("Total Amount = ",amt)
if (amt>=100000):
    dis=10
elif (amt>=50000):
    dis=5
elif (amt>=20000):
    dis=3

elif (amt>=10000):
    dis=2
else:
    dis=0
disamt=amt*dis/100
print("Discount Amount = ",disamt)
netamt=amt-disamt
print("Total Amount After Discount = ",netamt)
vt=netamt*0.13
print("Vat Amount",vt)
gt=netamt+vt
print("Grand Total = ",gt)


