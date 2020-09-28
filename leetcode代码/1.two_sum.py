
def twoSum(nums,target):
   length = len(nums)
   # nums.sort()
   for i in range(length-1):
       for j in range(length-1, i, -1):
           if nums[i] + nums[j] == target:
               return [i, j]

if __name__ == "__main__":
    nums = [3,2,4]
    index = twoSum(nums, 6)
    print(index)


