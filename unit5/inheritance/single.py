class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")

c = Child()
c.parent_method()  # Output: This is the parent method.
c.child_method()   # Output: This is the child method.
