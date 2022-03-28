from calendar import month
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# slope:
m = 8
# intercept:
b = 40

y = []
for x in months:
    result = x * m + b
    y.append(result)

print(y)

plt.plot(months, y)
plt.plot(months, revenue, "o")

plt.show()
