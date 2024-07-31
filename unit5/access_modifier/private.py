class MyClass:
    def __init__(self):
        self.__private_variable = "I am private"

    def __private_method(self):
        return "This is a private method"
    def access_private(self):
        return self.__private_variable, self.__private_method()

obj = MyClass()
# print(obj.__private_variable) # Raises an AttributeError
# print(obj.__private_method()) # Raises an AttributeError
    # print(obj.access_private()) # Accessible within the class