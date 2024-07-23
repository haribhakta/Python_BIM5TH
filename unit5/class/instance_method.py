class Car:
    # Initializer / Constructor
    def __init__(self, make, model, year, color):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Instance method to describe the car
    def description(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

    # Instance method to change the color of the car
    def paint(self, new_color):
        self.color = new_color

    # Instance method to calculate the age of the car
    def age(self, current_year):
        return current_year - self.year

    # Instance method to compare the age of two cars
    def is_older_than(self, other_car):
        return self.year < other_car.year

# Creating instances of the Car class
my_car = Car("Toyota", "Corolla", 2020, "Red")
your_car = Car("Honda", "Civic", 2019, "Blue")

# Accessing instance methods
print(my_car.description())  # Output: 2020 Red Toyota Corolla
print(your_car.description())  # Output: 2019 Blue Honda Civic

# Changing the color of my_car
my_car.paint("Black")
print(my_car.description())  # Output: 2020 Black Toyota Corolla

# Calculating the age of the cars
print(my_car.age(2024))  # Output: 4
print(your_car.age(2024))  # Output: 5

# Comparing the age of the cars
print(my_car.is_older_than(your_car))  # Output: False
