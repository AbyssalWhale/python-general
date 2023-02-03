class Point:
# __init__ - constructor. self - will always have refference in memory to new created instance
    def __init__(self, x, y):
        self.x = x
        self.y = y

#by default method should have at least 1 parameter. Self is good as example
    def draw(self):
        print(f"Points (X: {self.x} Y: {self.y})")


point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()
print(type(point))
print(isinstance(point, int))
