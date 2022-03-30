# Write your function here
def larger_list(list1, list2):
    larger = list1
    if(len(list1) >= len(list2)):
        larger = list1
    else:
        larger = list2
    return larger[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
