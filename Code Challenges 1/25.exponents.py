# Write your function here
def exponents(bases, powers):
    finalList = []
    for i in bases:
        for j in powers:
            finalList.append(i**j)
    return finalList


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
