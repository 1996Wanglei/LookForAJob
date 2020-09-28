def search(nums, target):
    low = 0
    high = len(nums) -1
    while(low <=high):
        middle = low + ((high-low)>>1)
        if nums[middle] == target:
            return middle
        else:
            if nums[low] <= nums[middle]:
                if target < nums[middle] and target >= nums[low]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if target <= nums[high] and target > nums[middle]:
                    low = middle + 1
                else:
                    high = middle-1
    return -1

if __name__=="__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    c=search(nums, target)
    print(c)