# Write your function here
def remove_middle(lst, start, end):
    arrayRange = list(range(start, end+1))
    numToBeRemoved = []
    for i in arrayRange:
        numToBeRemoved.append(lst[i])

    for i in numToBeRemoved:
        lst.remove(i)
    return lst


# Uncomment the line below when your function is done
#list = [4, 8, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# BETTER ANSWER
""" def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:] """
