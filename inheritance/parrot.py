# Write a program that implements single inheritance in Python by
# creating two classes "Animal" and "Bird". The "Animal" class
# should have class property species and instance properties name,
# age, and habitat. The "Bird" class should inherit from "Animal"
# class and have instance properties flight, beak_length, and feather_color.
# Create a third class "Parrot" which inherits from the "Bird" class.
# The "Parrot" class should have instance properties speech and a method
# describe which returns a string "I am a X-year old Y parrot with
# Z speech ability" where X is the age, Y is the name, and Z is the speech ability.


################################################################################################


class Animal:
    species = None

    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat


class Bird(Animal):
    def __init__(self, name, age, habitat, flight, beak_length, feather_color):
        super().__init__(name, age, habitat)
        self.flight = flight
        self.beak_length = beak_length
        self.feather_color = feather_color


class Parrot(Bird):
    def __init__(self, name, age, habitat, flight, beak_length, feather_color, speech):
        super().__init__(name, age, habitat, flight, beak_length, feather_color)
        self.speech = speech

    def display(self):
        return f"I am a {self.age} year old {self.name} parrot with {self.speech} speech ability"


P = Parrot("AB", 12, "dd", "hh", "jj", "w", "y")
print(P.display())
