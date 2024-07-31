class MyClass:
    def __init__(self):
        self.public_variable = "I am public"

    def public_method(self):
        return "This is a public method"

obj = MyClass()
print(obj.public_variable) # Accessible
print(obj.public_method()) # Accessible