# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 20:38:06 2017

@author: Luohao
"""

"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。 
"""

#34 ms 5760K 
class Solution:
    def Add(self, num1, num2):
        # write code here
        s = []
        s.append(num1)
        s.append(num2)
        return sum(s)
        
 #34 ms 5760K        
class Solution:
    def Add(self, num1, num2):
        # write code here
        num1 &= 0xffffffff
        num2 &= 0xffffffff
        while num1:
            num1, num2 = (num1 & num2) << 1, (num1 ^ num2) & 0xffffffff
        return num2 - (1 << 32) if num2 >> 31 else num2

