# program to show multiple inheritance
class Parent1:
    def method1(self):
        print("This is method1 from Parent1.")

class Parent2:
    def method2(self):
        print("This is method2 from Parent2.")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is the child method.")

c = Child()
c.method1()  # Output: This is method1 from Parent1.
c.method2()  # Output: This is method2 from Parent2.
c.child_method()  # Output: This is the child method.
