# WAP in python to create a class that have two method
# one os static method and another is instance method.

class MyClass:
    @staticmethod
    def add(a, b):
        a

        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def greet(name):
        return f"Hello, {name}!"

    def instance_method(self):
        print("This is an instance method.")


# Using static methods
print(MyClass.add(5, 3))  # Output: 8
print(MyClass.subtract(10, 4))  # Output: 6
print(MyClass.greet("Alice"))  # Output: Hello, Alice!

# Creating an instance of MyClass
obj = MyClass()

# Accessing static methods through the instance (not common practice, but possible)
print(obj.add(5, 3))  # Output: 8
print(obj.subtract(10, 4))  # Output: 6
print(obj.greet("Bob"))  # Output: Hello, Bob!

# Calling an instance method
obj.instance_method()  # Output: This is an instance method.
