def nextPermutation(nums):
        length = len(nums)
        flag = 0
        for i in range(length-1, 0, -1):
            if nums[i] > nums[i-1]:
                flag = 1
                index_low = i
                while(index_low < length and nums[index_low] > nums[i-1]):
                    index_low += 1
                tmp = nums[index_low-1]
                nums[index_low-1] = nums[i-1]
                nums[i-1] = tmp
                i_right = nums[i::]
                i_right.sort()
                for j in range(len(i_right)):
                    nums[i] = i_right[j]
                    i += 1
                break
        if flag == 0:
            nums.reverse()
        return nums
    
if __name__ == "__main__":
    nums = [1,5,1]
    nums = nextPermutation(nums)
    print(nums)