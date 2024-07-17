# # WAP in python to find area of volume using keyword argument.
# def area_volume(length,breadth,height):
#     v = length*breadth*height
#     return v
#
# l=float(input("Enter length = "))
# b=float(input("Enter breadth = "))
# h=float(input("Enter height = "))
# v=area_volume(length=l,breadth=b,height=h)
# print("Area of volume = ",v)

# WAP in Python to enter any three numbers into function
# and find its total and average.
def calculate(num1,num2,num3):
    t = num1+num2+num3
    a = t /3
    print ("Total = ",t)
    print("Average =",a)

a=int(input("Enter First Number = "))
b=int(input("Enter Second Number = "))
c=int(input("Enter Third Number = "))
calculate(num1=a,num2=b,num3=c)
