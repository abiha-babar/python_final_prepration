# class Square:
#     def __init__(self,length):
#         self._length = length

#     def __str__(self):
#         return f
# "Hello I am object of class Square with area {self.get_area()}".upper()

#     @property
#     def length(self):
#         return self._length

#     @length.setter
#     def length(self, length):
#         self._length  = length

#     def get_area(self):
#         return self._length * self._length

# def get_area():
#     pass

# a = Square(10)


# a.length = 50
# print(a)

# Hello I am object of class A with area 2500


# 1.  Write a program to define a class called Person with properties first_name and last_name,
#     and a method called full_name which returns the full name of a person.

# 2.  Write a program to define a class Rectangle with properties length and width, and methods
#     to calculate the area and perimeter of the rectangle.

# 3.  Write a program to define a class Circle with property radius and a method to calculate
#     the area and circumference of the circle.

# SOLVE FIRST QUESTION

# class Person :
#     def __init__ (self, first_name , last_name):
#         self._first_name = first_name
#         self.last_name = last_name

#     def full_name(self):
#         return  f"{self._first_name} {self.last_name}".upper()

#     @property
#     def first_name(self):
#         return self._first_name
#     @first_name.setter
#     def first_name(self,first_name):
#         self._first_name = first_name

# a= Person('abiha','babar')
# a.first_name= 'arisha'
# print(a.full_name())
