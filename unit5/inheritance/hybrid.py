# hybrid inheritance
class Base:
    def base_method(self):
        print("This is the base method.")

class Intermediate1(Base):
    def intermediate1_method(self):
        print("This is the intermediate1 method.")

class Intermediate2(Base):
    def intermediate2_method(self):
        print("This is the intermediate2 method.")

class Derived(Intermediate1, Intermediate2):
    def derived_method(self):
        print("This is the derived method.")


d = Derived()
d.base_method()           # Output: This is the base method.
d.intermediate1_method()  # Output: This is the intermediate1 method.
d.intermediate2_method()  # Output: This is the intermediate2 method.
d.derived_method()        # Output: This is the derived method.
