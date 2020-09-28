

def heap(nums, root, length):
    temp = nums[root]
    i = root * 2 + 1
    while (i < length):
        if i + 1 < length and nums[i+1] < nums[i]:
            i = i+1
        if temp > nums[i]: # 小根堆，父节点大要往下面调整
            nums[root] = nums[i]
        else:
            break
        root = i
        i = i * 2 +1
    nums[root] = temp
