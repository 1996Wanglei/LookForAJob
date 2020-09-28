
def searchInsert(nums,target):
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    low = 0
    high = len(nums) - 1
    while(low <= high):
        middle = low +((high - low)>>1)
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            low = middle +1
        else:
            high = middle-1
    return high + 1
if __name__ == "__main__":
    a = [1,3,5,6]
    target = 5.5
    index = searchInsert(a,target)
    print(index)