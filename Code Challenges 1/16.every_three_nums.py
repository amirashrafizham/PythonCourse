# Write your function here

def every_three_nums(start):
    list_num = []
    if start > 100:
        return list_num
    while(start <= 100):
        list_num.append(start)
        start += 3
    return list_num


# Uncomment the line below when your function is done
print(every_three_nums(91))


# BETTER ANSWER
""" def every_three_nums(start):
  return list(range(start, 101, 3)) """
