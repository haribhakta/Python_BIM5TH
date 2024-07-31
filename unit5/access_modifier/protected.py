class MyClass:
    def __init__(self):
        self._protected_variable = "I am protected"

    def _protected_method(self):
        return "This is a protected method"
class SubClass(MyClass):
    def access_protected(self):
        return self._protected_variable, self._protected_method()

obj = SubClass()
print(obj.access_protected()) # Accessible within the subclass