# WAP in python to find area of rectangle using positional
# passing argument
def trangle_area(base,height):
    a = 1/2*base*height
    return a

b = int(input("Enter Base = "))
h = int(input("Enter Height = "))
a = trangle_area(b,h)
print("Area of traingle = ",a)
