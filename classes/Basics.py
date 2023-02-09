from collections import namedtuple

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

    # will be used to compare objects of this type
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y


point = Point(1, 2)
point2 = Point(1, 2)
print(point.x)
print(point.y)
point.draw()

# Object attributes(varriables) are dynamic and can be defined everywhere
point.result = point.x + point.y
print(point.result)

# Check type
print(type(point))
print(f"Isinstance: {isinstance(point, int)}")
print(f"Issubclass: {issubclass(type(point), int)}")

# Check memory location
print(id(point))
print(id(point2))
print(point == point2)

# Tuple = To compare objects data. Object has the same tupe
TuplePoint = namedtuple("TuplePoint", ["x", "y"])
POINT_T = TuplePoint(x=1, y=2)
POINT_2_T = TuplePoint(x=1, y=2)
print(POINT_T == POINT_2_T)

# Varriable access
print(point.default_color)
print(Point.default_color)

# attribute(varriables) will be updated globally for all abjects
Point.default_color = "red"

print(point.default_color)
print(Point.default_color)

# __default_color_private - it private and next line will resie Exeption
# print(f"Default color hidden: {point.__default_color_private}")


# Extending Buil-It Types

# Extending string
class CustomStr(str):
    def duplicate(self):
        return self + self


text = CustomStr("Python")
print(text.lower())


# Extending append method for lists
class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


myList = TrackableList()
myList.append(1)
