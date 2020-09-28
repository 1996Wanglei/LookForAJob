def permute(nums):
    result = []
    n = len(nums)
    depth = 0
    used = [False for _ in range(n)]
    path = []
    nums.sort()
    dfs(nums, depth, path, used, n, result)
    return result

def dfs(nums, depth, path, used, n, result):
    if depth == n:
        result.append(path.copy())
        return
    for i in range(n):
        if not used[i]:
            if i > 0 and nums[i] == nums[i - 1] and used[i-1] :
                continue
            used[i] = True
            path.append(nums[i])
            dfs(nums, depth+1, path, used, n, result)
            used[i] = False
            path.pop()


if __name__ == "__main__":
    nums = [1,1,1,2]
    print(permute(nums))
