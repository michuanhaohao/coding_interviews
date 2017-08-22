# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:03:46 2017

@author: Luohao
"""

"""
输入一个整数，输出该数二进制表示中1的个数。
其中负数用补码表示。
"""

#33 ms 5768K 
class Solution:
    def NumberOf1(self, n):
        # write code here
        result = [ n>>i & 1 for i in range(0,32)]
        return sum(result)
        