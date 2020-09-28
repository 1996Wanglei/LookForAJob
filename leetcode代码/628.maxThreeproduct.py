def maxThreeproduct(nums):
    nums.sort()
    count_fushu = 0
    count_zhengshu = 0
    for i in range(len(nums)):
        if nums[i] >= 0:
            count_zhengshu +=1
        if nums[i] < 0:
            count_fushu += 1
    if count_zhengshu >=3 and count_fushu < 2:
        return nums[-1] * nums[-2] * nums[-3]
    elif count_fushu >= 2:
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2]*nums[-3])
    else:
        return nums[-1] * nums[-2] * nums[-3]

if __name__ == "__main__":
    nums = [-3,-3,0,0,2,3]
    print(maxThreeproduct(nums))
