# Write your max_num function here:

def max_num(num1, num2, num3):
    larger = num1
    if(larger > num2):
        larger = num1
    elif(larger < num2):
        larger = num2
    else:
        return "It's a tie!"

    if(larger > num3):
        larger = larger
        return larger
    elif(larger < num3):
        larger = num3
        return larger
    else:
        return "It's a tie!"


# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
