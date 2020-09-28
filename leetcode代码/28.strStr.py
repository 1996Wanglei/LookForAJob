#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (37.55%)
# Total Accepted:    36.4K
# Total Submissions: 96.8K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        def getnext(length_pattern,pattern):
            j = - 1
            next = list(range(len_needle))
            for i in range(length_pattern):
                while(j != -1 and pattern[i] != pattern[j+1]):
                    j = next[j]
                if pattern[i] == pattern[j+1]:
                    j += 1
                next[i] = j
            return next
        next = getnext(len_needle,needle)
        print(next)
        index = 0
        if len_needle == 0:
            return index
        j = -1
        for i in range(len_haystack):
            while(j != -1 and haystack[i] != needle[j+1]):
                j = next[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == len_needle -1:
                index = i + 1 - len_needle
                return index
        return -1

