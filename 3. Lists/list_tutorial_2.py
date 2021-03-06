from msilib import datasizemask


front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]

# insert value at specific index
front_display_list.insert(0, "Pineapple")
print(front_display_list)

# remove value at specific index
data_science_topics = ["Machine Learning", "SQL",
                       "Pandas", "Algorithms", "Statistics", "Python 3"]
data_science_topics.pop()
data_science_topics.pop(3)
print(data_science_topics)

# using range() and list()
number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# using specific range and skips
range_five_three = range(5, 15, 3)
print(list(range_five_three))

range_diff_five = range(0, 40, 5)
print(list(range_diff_five))

# checking the length of list
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that",
             "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

long_list_len = len(long_list)
print(long_list_len)

big_range = range(2, 3000, 100)
big_range_length = len(big_range)
print(big_range_length)

# slicing list
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]
middle = suitcase[2:4]
print(beginning)
print(middle)

# slicing list - first and last elements
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


# count number of elements
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie",
         "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)


# sort lists 1
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place",
             "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()

names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()
print(sorted_cities)

cities.sort(reverse=True)

# sort lists 2
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)
