# Write a program that creates a class Circle with a class attribute
#  pi set to 3.14 and an instance attribute radius set to 1.
# The class should have a method area that calculates the area of the
# circle and a method circumference that calculates the circumference of the circle.
# Finally, create an instance of the circle and print its area and circumference.


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self._radius = radius

    def area(self):
        return Circle.pi * self._radius**2

    def circumference(self):
        return round(2 * self.pi * self._radius, 3)


a = Circle(10)
print(a.area())
print(a.circumference())
