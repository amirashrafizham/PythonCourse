
# Accessing a Key

from collections import UserDict


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": [
    "Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}


print(zodiac_elements["earth"])
print(zodiac_elements["fire"])


# Check if a key exists or not, using If...In

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements)

# Check if a key exists or not, using Try/Except
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30

try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")


# A faster way to access key-pair and check if a key exists or not using .get()
user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)


# How to delete a key value using .pop()

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20,
                   "strength sandwich": 25, "stamina grains": 15, "power stew": 30}

health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

# Storing Keys only using .keys()

user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

# Storing Values only using .values()

total_exercises = 0
for i in list(num_exercises.values()):
    total_exercises += i

print(total_exercises)


# Storing both Keys and Values using .itmes()
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9,
                           "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
    print(f'Women make up {value} percent of {key}s')
