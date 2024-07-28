# program for multilevel
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")

c = Child()
c.grandparent_method()  # Output: This is the grandparent method.
c.parent_method()       # Output: This is the parent method.
c.child_method()        # Output: This is the child method.
