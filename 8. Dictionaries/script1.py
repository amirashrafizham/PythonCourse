# key-pair with strings
sensors = {"room_temp": 30, "room_humidity": 60}

translations = {"mountain": "orod", "bread": "bass",
                "friend": "mellon", "horse": "roch"}
print(translations)

# key-list pair

children = {"von Trapp": ["Johannes", "Rosmarie",
                          "Eleonore"],  "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

# How to create an empty dictionary
my_empty_dictionary = {}


# How to add a new item in a dictionary
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)


# How to add multiple new items in a dictionary
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})


# How to edit a key
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
                 "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

# print(oscar_winners)


# Combining 2 different lists into a dictionary
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]


# Using zip() method to create a Dictionary with 2 different lists
zipped_drinks = zip(drinks, caffeine)  # creates a tuple
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
