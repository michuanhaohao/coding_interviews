# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:52:08 2017

@author: Luohao
"""

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# 36 ms 5648K 
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 2:
            return number
        else:
            return 2 * self.jumpFloorII(number-1)  # 1+(n-1) or (n-1)+1
            
# 35 ms 5648K 
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return number
        else:
            return pow(2,number-1)