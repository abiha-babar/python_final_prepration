# Write a program to define a class Vehicle with properties make,
# model and year and a method display() which prints the make, model
# and year of the vehicle. Then, create a class Car that inherits from
# the Vehicle class and has additional property color and method
# display_color() which prints the make, model, year and color of the car.
# Finally, create an instance of the Car class and call both the display()
# and display_color() methods.

# Make: [make], Model: [model], Year: [year] --> for Vehicle
# Make: [make], Model: [model], Year: [year], Color: [color] --> for Car

######################################################################################


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def display_color(self):
        return super().display() + f" ,Color : {self.color}"


C1 = Car("Toyota", "Corola", 2020, "black")
print(C1.display())
print(C1.display_color())
