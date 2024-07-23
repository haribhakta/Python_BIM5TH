class Addition:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
    def putvalue(self):
        self.a = int(input("Enter a number = "))
        self.b = int(input("Enter another number = "))


    def sum(self):
        self.c = self.a + self.b
        return self.c
add = Addition()
add.putvalue()
print("Sum = ", add.sum())
# WAP in python to enter length and breadth of a rectangle
# and find its area by using class and object.

# WAP in python to create a class that ask data of two car
# (name,model and price)  then compare them with price.