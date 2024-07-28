class Myclass:
    def __init__(self,value="Optional Constructor"):
        self.value = value

    def display(self):
        print("The constructor value = ",self.value)


obj = Myclass()
obj.display()