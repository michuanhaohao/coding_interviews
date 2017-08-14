# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:22:22 2017

@author: Luohao
"""

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# over time
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        else:
            return self.jumpFloor(number-1) + self.jumpFloor(number-2) 
            
# 36 ms 5764K             
class Solution:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 1
        for i in range(number):
            a,b = b,a+b
        return a