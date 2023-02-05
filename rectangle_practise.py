from types import MethodType

# CLASSES

# WRITE A RECTANGLE CLASS
# - WITH 2 CONSTUCTOR VALUES LENGTH AND WIDTH (MAKE SURE USE PASS VALID value i.e value > 0 and must be a number)
# - calculate_area method which whill return the area of the rectangle. formula: length * width
# - calculate_perimeter of the rectangle. formula: 2 * (length + width)


class Rectangle:

    TOTAL_RECTANGLES = 0

    def __init__(self, length=0, width=0):
        self._width = width
        self._length = length
        Rectangle.TOTAL_RECTANGLES += 1

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

    def __str__(self):
        return f"Your rectangle has dimensions ({self._length}, {self._width})"

    def __eq__(self, rectangle):
        return self._length == rectangle._length and self._width == rectangle._width

    def __gt__(self, rectangle):
        return self.calculate_area() > rectangle.calculate_area()

    def __lt__(self, rectangle):
        return self.calculate_area() < rectangle.calculate_area()

    def __ge__(self, rectangle):
        return self.calculate_area() >= rectangle.calculate_area()

    def __le__(self, rectangle):
        return self.calculate_area() <= rectangle.calculate_area()

    def __ne__(self, rectangle):
        if isinstance(rectangle, Rectangle):
            return self.calculate_area() != rectangle.calculate_area()
        else:
            raise ValueError("Passed value must be a Rectangle")

    # def set_length(self, length):
    #     if type(length) in [int, float] and length >= 0:
    #         self._length = length
    #     else:
    #         raise ValueError("Length must be a number")

    # def get_length(self):
    #     return self._length

    # length = property(get_length, set_length)

    # def set_width(self, width):
    #     if type(width) in [int, float] and width >= 0:
    #         self._width = width
    #     else:
    #         raise ValueError("width must be a number")

    # def get_width(self):
    #     return self._width

    # width = property(get_width, set_width)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if type(width) in [int, float] and width >= 0:
            self._width = width
        else:
            raise ValueError("width must be number")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if type(length) in [int, float] and length >= 0:
            self._length = length
        else:
            raise ValueError("length must be number")

    @classmethod
    def total_rectangles(cls):
        return cls.TOTAL_RECTANGLES

    @staticmethod
    def get_perimeter(rectangle):
        if not isinstance(rectangle, Rectangle):
            raise Exception

        return rectangle.calculate_perimeter()


# WRITE A SQUARE CLASS
# length = int(input("Enter length :: "))
# width = int(input("Enter width :: "))


my_rec_1 = Rectangle(60, 20)  # Area: 200
my_rec_2 = Rectangle(10, 30)  # Area: 50

# my_rec_1.say_hellp = lambda self: self._length
my_rec_1.say_hello = MethodType(lambda self: self.width, my_rec_1)


print(my_rec_1.say_hello())
