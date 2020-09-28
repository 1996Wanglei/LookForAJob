#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.34%)
# Total Accepted:    88.1K
# Total Submissions: 268.8K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(0)
        p = r
        count = 0
        while(l1 and l2):
            tmp = ListNode(0)
            tmp.val = l1.val + l2.val if count == 0 else l1.val + l2.val +1
            count = 0
            if tmp.val >= 10:
                count = 1
                tmp.val -= 10
            p.next = tmp
            p = p.next
            l1 = l1.next
            l2 = l2.next 
        if count == 1 and l1 is None and l2 is None:
            tmp = ListNode(1)
            p.next = tmp
            p = p.next
            return r.next
        while l1:
            tmp = ListNode(0)
            tmp.val = l1.val if count == 0 else l1.val +1
            count = 0
            if tmp.val >= 10:
                count = 1
                tmp.val -= 10
            p.next = tmp
            p = p.next
            l1 = l1.next
        if count == 1:
            tmp = ListNode(1)
            p.next = tmp   
        while l2:
            tmp = ListNode(0)
            tmp.val =l2.val if count == 0 else l2.val +1
            count = 0
            if tmp.val >= 10:
                count = 1
                tmp.val -= 10
            p.next = tmp
            p = p.next
            l2 = l2.next
        if count == 1:
            tmp = ListNode(1)
            p.next = tmp  
        return r.next
         


            


