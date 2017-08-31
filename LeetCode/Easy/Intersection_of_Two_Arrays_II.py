'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
'''

# Counter：字典的子类，用于统计哈希对象。
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        n3 = n1 & n2 # 交集
        res = []
        for i in n3:
            res += [i] * min(n1[i], n2[i]) # i复制成list
        return res