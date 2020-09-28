def getPermutation(n, k):
    product = 1
    for i in range(1, n):
        product *= i
    if n == 1 or n == 2:
        start = k
        end = 1
    else:
        if k % product == 0:
            start = k // product
            end = product
        else:
            start = k // product + 1
            end = k % product

    result = []
    path = ""
    nums = [i for i in range(1, n + 1)]
    temp = nums[0]
    nums[0] = nums[start - 1]
    nums[start - 1] = temp
    right = nums[1:]
    right.sort()
    j = 1
    for i in range(len(right)):
        nums[j] = right[i]
        j += 1
    isUsed = [False for i in range(n)]
    count = 0
    print(start, nums)
    dfs(nums, n, result, path, isUsed, count, end)
    print(result)
    return result[end - 1]


def dfs(nums, n, result, path, isUsed, count, end):
    if len(path) == n:
        result.append(path)
        count += 1
        return

    for i in range(len(nums)):
        if not isUsed[i]:
            isUsed[i] = True
            path = path + str(nums[i])
            if len(result) < end:
                dfs(nums, n, result, path, isUsed, count, end)
                isUsed[i] = False
                path = path[:-1]
            else:
                return

if __name__ == "__main__":
    print(getPermutation(3,5))