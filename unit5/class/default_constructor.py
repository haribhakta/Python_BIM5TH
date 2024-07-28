class Myclass:
    def __init__(self):
        self.value = "This is default constructor"

    def display(self):
        print("The constructor value = ",self.value)


obj = Myclass()
obj.display()