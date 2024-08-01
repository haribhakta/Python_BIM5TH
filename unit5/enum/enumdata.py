
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum members
print(Color.RED)        # Output: Color.RED
print(Color.RED.name)   # Output: 'RED'
print(Color.RED.value)  # Output: 1

# Iterating through an enumeration
for color in Color:
    print(color)

# Comparing enum members
if Color.RED == Color.RED:
    print("They are the same color!")
