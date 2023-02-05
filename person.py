# Write a program that creates a class Person with a class attribute total_people
# set to 0 and an instance attribute name. The class should have a static method
# show_total_people that returns the value of total_people and an instance method
# say_hello that prints a message that says "Hello, I am [name]".
# Finally, create several instances of the Person class and call the static method
# to display the total number of people created.


class Person:
    total_people = 0

    def __init__(self, name):
        self.name = name
        Person.total_people += 1

    def say_hello(self):
        return f"Hello, I am {self.name}"

    @staticmethod
    def show_total_people():
        return Person.total_people


P1 = Person("Babar")
P2 = Person("Abiha")

print(Person.show_total_people())

print(P2.name, P1.name)
