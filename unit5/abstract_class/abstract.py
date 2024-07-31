from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Instantiate the subclasses
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow

# Attempting to instantiate the abstract class will raise an error
# animal = Animal()  # Raises TypeError: Can't instantiate abstract class Animal with abstract method make_sound
