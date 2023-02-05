# Write a program to define a class Animal with property name and
# method display() which prints the name of the animal. Then, create
# a class Bird that inherits from the Animal class and has additional
# property species and method display_species() which prints the name
# and species of the bird. Finally, create an instance of the Bird class
# and call both the display() and display_species() methods.class

###########################################################################


class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"I am from Animal class, My name is {self.name}"


class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_species(self):
        return super().display() + f" MY species is {self.species}"


B = Bird("Crow", "oookk")
print(B.display())
print(B.display_species())
