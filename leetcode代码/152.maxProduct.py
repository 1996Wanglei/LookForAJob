def maxProduct(nums):
    max_product = 1
    min_product = 1
    result = -10000000000
    for i in range(0, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(max_product * nums[i], nums[i])
        min_product = min(min_product * nums[i], nums[i])
        result = max(max_product, result)
    return result


if __name__ == "__main__":
    nums = [-2, 3, -4]
    print(maxProduct(nums))


