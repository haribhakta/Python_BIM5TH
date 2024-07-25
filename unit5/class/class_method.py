class MyClass:
    # Class attribute
    count = 0

    def __init__(self, value):
        self.value = value
        MyClass.count += 1


    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def create_with_value(cls, value):
        return cls(value)


    def display_value(self):
        print(f'Value: {self.value}')


# Create instances of MyClass
obj1 = MyClass.create_with_value(10)
obj2 = MyClass.create_with_value(20)

# Access class method
print(MyClass.get_count())  # Output: 2
# Access instance methods
obj1.display_value()  # Output: Value: 10
obj2.display_value()  # Output: Value: 20
