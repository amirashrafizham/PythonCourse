# Write your function here

def middle_element(lst):
    length = len(lst)
    print(length)
    if(length % 2 == 0):
        index1 = lst[int(length/2)]
        index2 = lst[int(length/2) - 1]
        element = (index1 + index2)/2
        return element
    else:
        index = int(length/2 - 0.5)
        element = lst[index]
        return element


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
