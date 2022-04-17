# Write your first_three_multiples function here
def first_three_multiples(num):
    final_number = 0
    for i in range(1, 4):
        final_number = i*num
        print(final_number)
    return final_number


# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
