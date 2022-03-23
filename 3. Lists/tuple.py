
# Tuple example

my_info = ('Amir', 28, "Software Engineer")

# Tuple works the same way as a List

name = my_info[0]
age = my_info[1]
role = my_info[2]

print(name)

# Another cool feature is that a Tuple can be unpacked easily
name1, age1, role1 = my_info


# The difference between Lists and Tuples is they're not immutable. Can't be changed (add, remove, sort etc.)

# Will print error
""" my_info[0] = 'Ashraf'
print(my_info) """
