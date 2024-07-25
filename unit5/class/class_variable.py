
class MyClass:
    # This is a class variable
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        # This is an instance variable
        self.instance_variable = instance_variable

    def display_variables(self):
        print("Class variable: ",MyClass.class_variable)
        print("Instance variable: ",self.instance_variable)

# Create two instances of MyClass
object1 = MyClass("Instance 1 variable")
object2 = MyClass("Instance 2 variable")

# Display the variables for both objects
object1.display_variables()
object2.display_variables()

# Modify the class variable using the class name
MyClass.class_variable = "Modified class variable"

# Display the variables again to see the change
object1.display_variables()
object2.display_variables()
