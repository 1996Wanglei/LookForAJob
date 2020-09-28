def maxSubarray(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    result = dp[0]
    for i in range(1, len(nums)):
        if dp[i-1] + nums[i] > nums[i]:
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = nums[i]
        if dp[i] > result:
            result = dp[i]
    return result
