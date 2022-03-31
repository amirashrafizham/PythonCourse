# Write your function here
def reversed_list(lst1, lst2):
    # Reverse List2
    reversedList = []
    negativeLength = (len(lst2)*-1)-1
    counter = -1
    while counter != negativeLength:
        reversedList.append(lst2[counter])
        counter -= 1

    # Check List1 and List2 same
    trueCounter = 0
    for i in range(len(lst1)):
        if(lst1[i] == reversedList[i]):
            trueCounter += 1

    if(trueCounter == len(lst1)):
        return True

    return False


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# A BETTER SOLUTION
""" def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True """
