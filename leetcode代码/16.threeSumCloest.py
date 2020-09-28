def threeSumCloest(nums, target):
    length = len(nums)
    if length < 3:
        return nums
    count = 9223372036854775807
    nums.sort()
    for i in range(length-2):
        low = i+1
        high = length-1
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        while low < high:
            value = nums[i] + nums[low] + nums[high]
            if (abs(value - target) < abs(count - target)):
                count = value
            if value == target:
                return target
            else:
                if value > target:
                    high -= 1
                if value < target:
                    low += 1
    return count


if __name__ == "__main__":
    nums = [1,2,4,8,16,32,64,128]
    target = 82
    s = threeSumCloest(nums, target)
    print(s)

