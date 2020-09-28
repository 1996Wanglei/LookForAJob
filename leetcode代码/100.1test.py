def findKthLargest(nums, k):
    for i in range(k // 2 - 1, -1, -1):
        Heap(nums, i, k)
    for j in range(k, len(nums)):
        if nums[j] > nums[0]:
            nums[0] = nums[j]
            Heap(nums, 0, k)
    print(nums)
    return nums[0]


def Heap(nums, root, length):
    temp = nums[root]
    i = root * 2 + 1
    while (i < length):
        if i + 1 < length and nums[i + 1] < nums[i]:
            i += 1
        if nums[root] > nums[i]:
            nums[root] = nums[i]
        else:
            break
        root = i
        i = i * 2 + 1
    nums[root] = temp

if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    findKthLargest(nums, k)

