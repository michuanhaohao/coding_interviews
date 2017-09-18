# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:57:28 2017

@author: Luohao
"""


"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""

class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        def addN(n):
            self.sum = self.sum + n
            n = n -1
            return n>0 and self.Sum_Solution(n)
            
        addN(n)
        
        return self.sum
        
n=10       
s = Solution()
a= s.Sum_Solution(n)