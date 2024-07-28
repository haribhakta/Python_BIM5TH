class Myclass:
    def __init__(self,value):
        self.value = value

    def display(self):
        print("The constructor value = ",self.value)


obj = Myclass("I am value for constructor")
obj.display()