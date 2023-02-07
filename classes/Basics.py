# pass - to create just empty class
class EmptyClass:
    pass


class Point:
    # This attributes (varriable) are always static
    default_color = "blue"

    # This attributes (varriable) is always private
    __default_color_private = "purple"

    # __init__ - constructor. self - will always have refference in memory to new created instance
    def __init__(self, x, y):
        self.x = x
        self.y = y

# by default method should have at least 1 parameter. Self is good as example
    def draw(self):
        print(f"Points (X: {self.x} Y: {self.y})")


point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()

# Object attributes(varriables) are dynamic and can be defined everywhere
point.result = point.x + point.y
print(point.result)

print(type(point))
print(f"Isinstance: {isinstance(point, int)}")
print(f"Issubclass: {issubclass(type(point), int)}")

print(point.default_color)
print(Point.default_color)

# attribute(varriables) will be updated globally for all abjects
Point.default_color = "red"

print(point.default_color)
print(Point.default_color)

print(f"Default color hidden: {point.__default_color_private}")
