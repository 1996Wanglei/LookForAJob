
def firstMissingPositive(nums):
    for i in range(len(nums)):
        while(nums[i] > 0 and nums[i] < len(nums)):
            temp = nums[nums[i]-1]
            nums[nums[i]-1] = nums[i]
            nums[i] = temp
    flag = 0
    for j in range(len(nums)):
        if nums[j] != j:
            flag = 1
            return j
    if flag == 0:
        return len(nums)
