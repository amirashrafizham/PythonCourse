# Write your large_power function here:


# Uncomment these function calls to test your large_power function:

from numpy import true_divide


def large_power(num1, num2):
    num = num1**num2
    if num > 5000:
        return True
    else:
        return False


print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
