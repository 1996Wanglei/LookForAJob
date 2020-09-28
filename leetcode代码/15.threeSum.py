
def threeSum(nums):
    list = []
    if len(nums) < 3:
        return []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] >0:
            break
        low = i+1
        high = len(nums)-1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while(low < high):
            value = nums[i] + nums[low] + nums[high]
            # if low == i:
            #     low += 1
            #     continue
            # if high == i:
            #     high -= 1
            #     continue
            if value == 0:
                list.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while(low < high and nums[low] == nums[low-1]):
                    low += 1
                while(high > low and nums[high] == nums[high+1]):
                    high -= 1
            if value > 0:
                high -= 1
            if value < 0:
                low += 1
    return list

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    list = threeSum(nums)
    print(list)