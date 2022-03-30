# Write your function here

def append_sum(lst):
    for i in range(3):
        num = lst[-1] + lst[-2]
        lst.append(num)
    return lst


# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
