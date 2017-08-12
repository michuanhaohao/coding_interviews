# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:30:37 2017

@author: Luohao
"""

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""
#28 ms	5760K
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            s = []
            s.append(1)
            s.append(1)
            for i in range(2,n):
                s.append(s[i-1]+s[i-2])
            return s[n-1]

# 算法没错，但是超时
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)
            
s = Solution()
result = s.Fibonacci(10)