from re import I


last_semester_gradebook = [["politics", 80], [
    "latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 75, 88]

gradebook = [["physics", 98], ["calculus", 97],
             ["poetry", 75], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

print(gradebook)

gradebook[-1][-1] += 5

print(gradebook)

gradebook[2].remove(75)
gradebook[2].append("Pass")

print(gradebook)


full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
