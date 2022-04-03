# Using type() function
from sklearn.cluster import k_means


print(type(5))


my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))


# Creating a Class
class Facade:
    pass


# Checking the type of Class. __main__  is similar to Main() method in C#. It tells the user that this is the Main() running, just that in C# this is implemented implicityly
facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)


# Fields
class Grade:
    minimum_passing = 65

# Methods


class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


# Constructors
""" class Circle:
    def __init__(self, diameter):
        print(f"New circle with diameter: {diameter}")

    pi = 3.14

    def area(self, radius):
        return Circle.pi*radius**2 """

# Instance Variables


class Store:
    store_name = ""

    def __init__(self, store_name):
        self.store_name = store_name


alternative_rocks = Store("Alternative Rocks")
isabelles_ices = Store("Isabelle's Ices")

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for i in can_we_count_it:
    if (hasattr(i, "count")):
        print(str(type(i)) + " has the count attribute!")
    else:
        print(str(type(i)) + " does not have the count attribute :(")


""" class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter/2

    def circumference(self):
        return 2*self.pi*self.radius 


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference()) """


# Using dir() to check attributes of an object
dir(5)


def this_function_is_an_object(stringObject):
    return stringObject


print(dir(this_function_is_an_object))


# Using __repr__ to return the class as a string

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def __repr__(self):
        return f"Circle with radius {self.radius}"

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)
