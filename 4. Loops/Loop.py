# For Loop basic structure
board_games = ["Settlers of Catan", "Carcassone",
               "Power Grid", "Agricola", "Scrabble"]

""" for item in board_games:
    print(item) """

for item in range(6):
    print(f"Current iteration: {item}")


# While Loop basic structure

count = 0
while count <= 3:
    count += 1

count = 10
while count >= 0:
    count -= 1

python_topics = ["variables", "control flow", "loops", "modules", "classes"]
count = 0
arrLength = len(python_topics)

while count < arrLength:
    print(f"I am learing {python_topics[count]}")
    count += 1

# Breaking Loops
dog_breeds_available_for_adoption = [
    "french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

# Continue Loops
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
    if i < 21:
        continue
    print(i)


# Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
    print(location)
    for j in location:
        scoops_sold += j
        print(f"scoops sold: {scoops_sold}")

print(scoops_sold)

# List Comprehension Part 1 : Introduction
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [i + 10 for i in grades]

print(scaled_grades)


# List Comprehension Part 2 : With Conditionals
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [i for i in heights if i > 161]

print(can_ride_coaster)

# Final Exercise
single_digits = list(range(0, 10))

squares = []


for i in single_digits:
    squares.append(i**2)
    print(i)

cubes = [i**3 for i in single_digits]

print(squares)
print(cubes)
