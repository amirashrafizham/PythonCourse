# Write your function here

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for j in lst2:
        sum2 += j
    if(sum1 > sum2):
        return lst1
    elif(sum1 < sum2):
        return lst2
    else:
        return lst1


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
