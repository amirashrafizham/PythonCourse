# Write your function here
def odd_indices(lst):
    newArray = []
    for i in lst:
        if(i % 2 != 0):
            newArray.append(i)

    return newArray


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
