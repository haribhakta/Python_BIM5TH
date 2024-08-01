class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)
print(p2)
print(p1 + p2)