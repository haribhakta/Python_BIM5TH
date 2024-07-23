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

