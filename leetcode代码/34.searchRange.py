
def searchRange(nums, target):
    low = 0
    high = len(nums)-1
    if len(nums) < 0:
        return [-1,-1]
    if len(nums) == 1 and nums[0] ==target:
        return [0,0]
    elif len(nums) == 1 and nums[0] ==target:
        return [-1,-1]
    while(low <= high):
        middle = low + ((high-low) >> 1)
        if nums[middle] >= target:
            high = middle -1
        else:
            low = middle + 1
    index = high + 1 if high != len(nums)-1 and nums[high+1] == target else -1
    if index == -1:
        return [-1, -1]
    else:
        j = index
        while(j < len(nums) and nums[index] == nums[j]):
            j += 1
        return [index, j-1]

if __name__ == "__main__":
    nums = [2,2,3]
    target = 3
    c = searchRange(nums,target)
    print(c)