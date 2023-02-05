# Write a program that implements multiple inheritance in Python by creating two
# classes "Food" and "Cuisine". The "Food" class should have class property category
# and instance properties name, ingredients, and cooking_time.
#
# The "Cuisine" class  should have class property style and instance
# properties spicy, vegetarian, and gluten_free. Create a third class
# "Recipe" which inherits from both "Food" and "Cuisine" classes.
#
# The "Recipe" class should have instance property servings and a method describe which
# returns a string "I am a X serving Y dish with Z ingredients" where X is the number of servings,
# Y is the name of the dish, and Z is the ingredients. It should also return "It is spicy,"
# "It is vegetarian," or "It is gluten-free" if the recipe has those respective characteristics.

##########################################################################################################


class Food:
    category = "food"
    __slot__ = ("name", "ingredients", "cooking_time")

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time


class Cuisine:
    style = "cuisine"

    def __init__(self, spicy, vegetarian, gluten_free):
        self.spicy = spicy
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free


class Recipe(Food, Cuisine):
    def __init__(
        self, name, ingredients, cooking_time, spicy, vegeterian, gluten_free, servings
    ):
        Food.__init__(self, name, ingredients, cooking_time)
        Cuisine.__init__(self, spicy, vegeterian, gluten_free)
        self.servings = servings

    def display(self):
        result = f"I am a {self.servings} servings, {self.name} Dish and {self.ingredients} ingredientse."
        if self.spicy:
            result += " It is spicy."
        if self.vegetarian:
            result += " It is vegeterian."
        if self.gluten_free:
            result += " It is gluten_free"

        return result


recipe = Recipe(
    "Spaghetti Bolognese",
    "spaghetti, ground beef, tomatoes, onions, garlic, herbs",
    30,
    True,
    True,
    True,
    4,
)
print(recipe.display())
