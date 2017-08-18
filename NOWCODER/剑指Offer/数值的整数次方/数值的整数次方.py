# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:33:39 2017

@author: Luohao
"""

"""
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
"""

#40 ms 5764K 
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent >=0:
            result = 1
            for i in range(exponent):
                result = result*base
            return result
        else:
            return 1./self.Power(base,-exponent)

            
s = Solution()
a= s.Power(0,0)