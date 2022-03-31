# Write your function here
def max_num(nums):
    nums.sort()
    maxNum = nums[0]
    for i in nums:
        if(i > maxNum):
            maxNum = i

    return maxNum


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
