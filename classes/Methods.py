class Point:

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Factory Method
    @classmethod
    def zero(cls):
        # Calling Point class constructor
        return cls(0, 0)

    # Magic Method
    def __str__(self) -> str:
        return f"(X: {self.x} Y: {self.y})"

# Factory Methods - methods returns new istance of class. Must have decorator @classmethod. CLS - is var with refference to class itself
point = Point.zero()
print(point.x, point.y)

# Magic Methods - has 2 unnderscors in the name and they are called automatically by python interpretator once object is initiated. https://rszalski.github.io/magicmethods/
point = Point(1, 2)
print(point)
