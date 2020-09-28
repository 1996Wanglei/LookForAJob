def productExceptself(nums):
    product_left = [1 for _ in range(len(nums))]
    product_right = [1 for _ in range(len(nums))]
    result = []
    for i in range(1, len(nums)):
        product_left[i] = nums[i-1] * product_left[i-1]
    for j in range(len(nums)-2, -1, -1):
        product_right[j] = nums[j+1] * product_right[j+1]
    for k in range(len(nums)):
        result.append(product_right[k] * product_left[k])
    return result

if __name__ == "__main__":
    nums = [1,2]
    print(productExceptself(nums))

