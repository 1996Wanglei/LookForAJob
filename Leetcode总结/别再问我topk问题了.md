##### 别再问我topk问题了

#### [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

在未排序的数组中找到第 **k** 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素

- 全局排序法

快速排序，然后直接输出第k个最大的元素，时间复杂度O(nlogn)

- 冒泡法

如果k比较小，考虑用冒泡法

```python
class Solution:
    def findKthLargest(self, nums: List[int], m: int) -> int:
        k = 0
        if len(nums) == m:
            return min(nums)
        max_x = -99999999999999
        while(k < m):
            index_max = 0
            for i in range(k, len(nums)):
                if nums[i] >= max_x:
                    max_x = nums[i]
                    index_max = i
            nums[k], nums[index_max] = nums[index_max], nums[k]
            k += 1
            max_x = -99999999999999
        return nums[m-1]
```

- 来自快排分片+减治的算法

主要的算法思想是，快速排序每次都会将一个元素放到最终排序数组中正确的位置，保证比这个元素小的所有元素都放在该元素的左边位置，比该元素大的元素都会放在该元素右边的位置。如果我们恰好找到这个位置就是第k个最大元素的位置，那么就可以直接返回。如果不是则到这个位置的左边或者右边继续寻找。算法复杂度为O(2n)

```python
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums)-1
        return self.RS(nums, low, high, len(nums)-k) #第k个最大的元素就是第len(nums)-k个最小的元素

    def RS(self, nums, left, right, k):
        if left == right:
            return nums[left]
        pivot_index = random.randint(left, right) # 随机选择一个元素，如果选用最右面的元素，在极端的情况下快速排序会退化到O(n2)

        pivot_index = self.partion(nums, left, right, pivot_index)
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index > k:
            return self.RS(nums, left, pivot_index-1, k) #在pivot的左边继续寻找
        elif pivot_index < k:
            return self.RS(nums, pivot_index+1, right, k)
    
    def partion(self, nums, left, right,  pivot_index):
        pivot = nums[pivot_index]
        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot: #小于nums[pivot]的都放在nums[pivot]的左边
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[right], nums[store_index] = nums[store_index], nums[right] #将nums[pivot]放到正确的位置, 比nums[pivot]小的元素都在最左边，比nums[pivot]大的元素都在最右边
        return store_index # 返回nums[pivot]的位置
```

- 建立一个k大小的小根堆。

这个小根堆中保存数组中最大的k个元素，其中第k大的元素放在堆顶。建堆是O(k)的复杂度，调整一次堆的时间复杂度是O(logk)

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k//2 -1, -1, -1):
            self.Heap(nums, i, k) #建立一个k个大小的小根堆
        for j in range(k, len(nums)): 
            if nums[j] > nums[0]: #如果当前元素比堆顶元素大，将其入堆，并且调整堆
                nums[0], nums[j] = nums[j], nums[0]
                self.Heap(nums, 0, k)
        # print(nums)
        return nums[0]

    def Heap(self, nums, root, length):
        temp = nums[root]
        i = root * 2 + 1
        while(i < length): # 寻找堆顶元素正确位置的循环
            if i + 1 < length and nums[i+1] < nums[i]: # 左右子结点谁更小
                i += 1
            if temp > nums[i]:  # 子结点比父节点更小，需要将子结点调整到父节点位置
                nums[root] = nums[i]
            else: #寻找完毕
                break
            root = i # 在该父节点上继续调整
            i = i * 2 + 1 #下一个子结点
        nums[root] = temp # 堆顶元素的最终位置
```

