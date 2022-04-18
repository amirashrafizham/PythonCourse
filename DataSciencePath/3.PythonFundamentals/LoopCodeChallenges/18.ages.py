names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

combined = zip(names, ages)

users = [f"Name: {name}, Age: {age}" for (name, age) in combined]
print(users)
