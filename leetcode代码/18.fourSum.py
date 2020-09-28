
def fourSum(nums, target):
    length = len(nums)
    list = []
    if length < 4:
        return list
    nums.sort()
    for i in range(length-3):
        left = i+1
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        for j in range(left, length-2):
            if j > left and nums[j] == nums[j-1]:
                j += 1
                continue
            middle = j+1
            right = length - 1
            while(middle < right):
                value = nums[i] + nums[j] +nums[middle] + nums[right]
                if target == value:
                    list.append([nums[i], nums[j], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    while(middle < right and nums[middle] == nums[middle-1]):
                        middle += 1
                    while(middle < right and nums[right] == nums[right +1]):
                        right -= 1
                elif target < value:
                    right -= 1
                else:
                    middle += 1
    return list

if __name__=="__main__":
    nums = [0,0,0,0]
    list = fourSum(nums, 0)
    print(list)