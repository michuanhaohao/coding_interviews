# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:00:16 2017

@author: Luohao
"""

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

#30 ms 5764K 
class Solution:
    def reOrderArray(self, array):
        # write code here
        ji = []
        ou = []
        for value in array:
            if (value % 2) == 1:
                ji.append(value)
            else:
                ou.append(value)
        result = ji + ou
        return result
        
s = Solution()
a = s.reOrderArray([1,2,3,5,6,4])        