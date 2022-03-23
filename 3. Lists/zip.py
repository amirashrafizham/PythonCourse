# Zip allows you to combine 2 separate Lists

from lib2to3.pytree import convert


owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

# However you can't simply print the combined Lists
print(names_and_dogs_names)


# To print, you must convert it
converted_list = list(names_and_dogs_names)
print(converted_list)
