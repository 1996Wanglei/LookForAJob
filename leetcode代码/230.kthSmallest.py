# 思路，用非递归中序遍历找到第k小的元素 
# 利用递归来寻找第k小的元素，先寻找左子树的结点数目leftN， 
# 如果leftN+1 > k,说明k小的元素在左子树，那么继续在左子树中寻找k小的元素，
# 如果leftN+1=k，说明第k小的元素就是当前的结点， 
# 如果leftN+1 < k, 说明第k小的元素元素在右子树当中，继续在右子树当中寻找k-leftN-1小的元素

import random

def kthSmallest(root, k):
    stack = []
    nums_node = 0
    cur = root
    while(cur is not None or len(stack)>0):
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            nums_node += 1
            if nums_node == k:
                return cur.val
            cur = cur.right

def 2thSmallest(root):
    stack = []
    cur = root
    max_val = root.val
    second_val = root.val
    flag = 0
    while(cur is not None or len(stack) > 0):
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if cur.val > max_val:
                flag = 1
                second_val = max_val
                max_val = cur.val
            cur = cur.right
    if flag == 1:
        return second_val
    else:
        return -1
    


def kthSmallest(root, k):
    leftN = findChildCount(root.left)
    if leftN+1 == k:
        return root.val
    if leftN+1 < k:
        return kthSmallest(root.right, k-leftN-1)
    if leftN+1 > k:
        return kthSmallest(root.left, k)

def findChildCount(root):
    if root is None:
        return 0
    return findChildCount(root.left)+findChildCount(root.right)+1
    

# 寻找一个有序队列中第k大的元素，也就是寻找一个有序队列中len(str)-k大的元素，我们用快速排序中分片的思想来解决这个问题。

def partion(pivot_index,nums, left, right):
    pivot = nums[pivot_index]
    nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
    less_index = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[less_index] = nums[less_index], nums[i] # 如果比pivot小，要把这些元素放在pivot的左边
            less_index += 1
    nums[right] , nums[less_index] = nums[less_index], nums[right] # pivot 最终的位置，它的右边全部是大于pivot的元素
    return less_index 

def RS(nums, left, right, k):
    if left == right:
        return nums[left]
    pivot_index = random.randint(left, right)
    pivot_index = partion(pivot_index, nums, left, right)
    #print(pivot_index)
    if pivot_index == k:
        return nums[pivot_index]
    elif pivot_index < k:
        return RS(nums, pivot_index+1, right, k)
    else:
        return RS(nums, left, pivot_index-1, k)

def Heap(nums, root, length):
    temp = nums[root]
    i = 2 * root + 1
    while(i < length):
        if i + 1 < length and nums[i+1] < nums[i]:  # 小根堆，找出子结点中较小的一个
        # if i + 1 < length and nums[i+1] > nums[i]:  # 大根堆，找出子结点中较大的一个
            i += 1
        if nums[i] < temp: # 如果子结点中最小的比父节点小，那么应该把这个结点放到父节点去，然后继续向下寻找
        # if nums[i] > temp:  #如果子结点中最大的一个比父节点大，那么应该把这个结点放到父节点去，然后继续向下寻找
            nums[root] = nums[i]
        else:
            break
        root = i
        i = i*2 + 1
    nums[root] = temp

def heap_sort(nums, k):
    for i in range(k//2-1, -1, -1):  # 建立一个K个元素的小根堆
        Heap(nums, i, k)
    for j in range(k, len(nums)):
        if nums[j] > nums[0]:
            nums[0], nums[j] = nums[j], nums[0]
            Heap(nums, 0, k)

if __name__ == "__main__":
    nums = [4,3,2,0,5,33,22,10]
    heap_sort(nums, 2)
    print(nums)

