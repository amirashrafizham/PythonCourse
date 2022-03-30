# Write your function here
def more_frequent_item(lst, item1, item2):
    count_item1 = lst.count(item1)
    count_item2 = lst.count(item2)

    print(count_item1)
    print(count_item2)
    if(count_item1 >= count_item2):
        return item1
    else:
        return item2


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
