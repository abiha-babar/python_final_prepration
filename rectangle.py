# 2.  Write a program to define a class Rectangle with properties length and width, and methods
#     to calculate the area and perimeter of the rectangle.


class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._length

    def perimeter(self):
        return (self._length + self._width) * 2

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    width = property(get_width, set_width)

    def __str__(self):
        return f"Area: {self.area()}, Perimeter: {self.perimeter()}"

    def __eq__(self, rectangle):
        if not isinstance(rectangle, Rectangle):
            raise ValueError

        return self._length == rectangle.length and self._width == rectangle.width


a = Rectangle(10, 5)
b = Rectangle(10, 5)

print(a == b)


# obj = Rectangle(10, 5)
# print(obj) --> Area: 50, Perimeter: 30

# 1. length -> decorator
# 2. width -> old_methond
