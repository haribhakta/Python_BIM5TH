
class Number:
    # class variable
    n = None
    def check(self):
        if Number.n % 2 == 0:
            print("It is Even")
        else:
            print("It is odd")


n = int(input("Enter a number = "))
Number.check()
