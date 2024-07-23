# creating and accessing instance variable
class Car:
    # Initializer / Constructor
    def __init__(self, make, model, year, color):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Method to describe the car
    def description(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

    # Method to change the color of the car
    def paint(self, new_color):
        self.color = new_color

# Creating instances of the Car class
my_car = Car("Toyota", "Corolla", 2020, "Red")
your_car = Car("Honda", "Civic", 2019, "Blue")

# Accessing instance variables
print(my_car.description())  # Output: 2020 Red Toyota Corolla
print(your_car.description())  # Output: 2019 Blue Honda Civic

# Changing the color of my_car
my_car.paint("Black")
print(my_car.description())  # Output: 2020 Black Toyota Corolla
