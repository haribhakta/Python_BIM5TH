class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self):
        return abs(self.x) + abs(self.y)

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)          # Output: Point(1, 2)
print(p1 == p2)    # Output: False
print(p1 + p2)     # Output: Point(4, 6)
print(len(p1))     # Output: 3
