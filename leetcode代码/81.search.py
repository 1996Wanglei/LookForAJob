def search(nums, target):
    left = 0
    right = len(nums)-1
    while(left <= right):
        mid = left + ((right-left)>>1)
        if nums[mid] == target :
            return True
        print(left, mid, right)
        if nums[left] < nums[mid]:
            if target < nums[mid] and target >= nums[left]:
                right = mid-1
            else:
                left = mid +1
        elif nums[right] > nums[mid]:
            if target <= nums[right] and target > nums[mid]:
                left = mid +1
            else:
                right = mid -1
        else:
            if nums[left] == nums[mid]:
                left += 1
            else:
                right -= 1
    return False

if __name__ == "__main__":
    #nums = [2,5,6,0,0,1,2,2,2,2,2,2,2]
    nums = [1,1,3,1]
    target = 3
    print(search(nums, target))