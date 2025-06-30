def add(*nums):
    sum_val = 0
    for i in range(len(nums)):
        sum_val += nums[i]
    return sum_val

print(add(100 , 200 , 300))
    