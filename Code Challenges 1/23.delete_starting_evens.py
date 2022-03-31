# Write your function here

def delete_starting_evens(lst):
    counter = 0
    lengthList = len(lst)
    while counter < lengthList:
        if(lst[0] % 2 == 0):
            lst.remove(lst[0])
        counter += 1
    return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
