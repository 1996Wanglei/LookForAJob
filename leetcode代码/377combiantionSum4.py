def combinationSum4(nums, target):
    """
    dp[i] 表示使用nums数组中数进行组合，其和为i的组合数目
    比如说 nums=[1, 3, 4]， target=7, dp[7] = dp[7-1] + dp[7-3] + dp[7-4] = dp[6] + dp[4] + dp[3]
    dp[1] = dp[0] + 1, 因为nums里面有1这个数， 所以dp[0] = 1
    """
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for i in range(1, target+1):
        print(dp[i-1])
        for j in range(len(nums)):
            if i >= nums[j]:
                dp[i] += dp[i-nums[j]]
    return dp[target]

if __name__ == "__main__":
    nums = [2, 3]
    target = 5
    print(combinationSum4(nums, target))

