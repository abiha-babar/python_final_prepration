# Write a program to define a class Circle with property radius and a method to calculate
# the area and circumference of the circle.


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * self._radius * self._radius

    def circumference(self):
        return round(2 * 3.14 * self._radius, 2)

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    radius = property(get_radius, set_radius)


a = Circle(9)
print(a.circumference(), a.area())
a.radius = 19
print(a.circumference(), a.area())
