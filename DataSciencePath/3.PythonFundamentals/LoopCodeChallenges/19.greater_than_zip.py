a = [30, 42, 10]
b = [15, 16, 17]

combined = zip(a, b)

greater_than = [a > b for (a, b) in combined]

print(greater_than)
