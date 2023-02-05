# Write a program that implements single inheritance in Python by creating two classes
# "HouseholdItem" and "Appliance". The "HouseholdItem" class should have class property
# category and instance properties name, brand, and price. The "Appliance" class should
# inherit from "HouseholdItem" class and have instance properties power_consumption, type,
# and warranty. Create a third class "Refrigerator" which inherits from the "Appliance" class.
# The "Refrigerator" class should have instance properties capacity and a method describe
# which returns a string "I am a X brand Y model refrigerator with Z capacity and W warranty"
# where X is the brand, Y is the name, Z is the capacity, and W is the warranty.


###############################################################################################


class HouseholdItem:
    category = None

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Appliance(HouseholdItem):
    def __init__(self, name, brand, price, power_cons, type, warranty):
        super().__init__(name, brand, price)
        self.power_cons = power_cons
        self.type = type
        self.warranty = warranty


class Refrigerator(Appliance):
    def __init__(self, name, brand, price, power_cons, type, warranty, capacity):
        super().__init__(name, brand, price, power_cons, type, warranty)
        self.capacity = capacity

    def display(self):
        return f"I am a {self.name} brand {self.brand} model refrigerator with {self.capacity} capacity and {self.warranty} warranty"


R = Refrigerator("AB", "kk", 6789, 55, "ddd", 1, 666)
print(R.display())
