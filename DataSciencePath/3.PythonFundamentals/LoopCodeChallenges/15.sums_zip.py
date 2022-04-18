a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

combined = zip(a, b)

sums = [a+b for (a, b) in combined]
print(sums)
