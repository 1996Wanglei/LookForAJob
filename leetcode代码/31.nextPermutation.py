
def nextPermutation(nums):
    length = len(nums)
    flag = 0
    for i in range(length-1, 1, -1):
        if nums[i] > nums[i-1]:
            flag = 1
            index_low = i
            for j in range(index_low, length):
                if nums[j] >= nums[i-1] and j == length-1:
                    tmp = nums[i-1]
                    nums[i - 1] = nums[j]
                    nums[j] = tmp
                elif nums[j] >= nums[i-1]:
                    continue
                else:
                    tmp = nums[i-1]
                    nums[i-1] = nums[j-1]
                    nums[j-1] = tmp
                    nums[j:].sort()
    if flag == 0:
        nums.reverse()
    return nums
if __name__=="__main__":
    nums = [1, 3, 4, 2]
    nums = nextPermutation(nums)
    print(nums)