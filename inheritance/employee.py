# Write a program to define a class Person with properties name and age,
# and a method display() which prints the name and age of the person.
# Then, create a class Employee that inherits from the Person class and
# has additional property salary and method display_salary() which prints
# the name, age and salary of the employee. Finally, create an instance of
# the Employee class and call the display() and display_salary() methods.

# Hello I am [name], my age is [age]  -> Display function of Person
# Hello I am [name], my age is [age] and my salary is [salary] -> Display function of Employee

################################################################################################


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Hello I am {self.name}, my age is {self.age}"


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        return super().display() + f" and my salary is {self.salary}"


E1 = Employee("abiha", 20, 69000)
print((E1.display()))
