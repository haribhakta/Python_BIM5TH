class Animal:
    def speak(self):
        print("The animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("The dog barks")
class Cat(Animal):
    def speak(self):
        print("The cat meows")
# Create instances of each class
generic_animal = Animal()
dog = Dog()
cat = Cat()
# Call the speak method on each instance
generic_animal.speak() # Output: The animal makes a sound
dog.speak() # Output: The dog barks
cat.speak()