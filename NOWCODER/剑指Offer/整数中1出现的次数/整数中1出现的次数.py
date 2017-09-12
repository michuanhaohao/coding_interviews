# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:28:47 2017

@author: Luohao
"""

"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。
"""

#28 ms 5768K 
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        result = 0
        base = 1
        roun = n
        while roun > 0:
            weight = roun%10
            roun = roun/10
            result = result + roun*base
            if weight == 1:
                result = result+ (n%base) + 1
            if weight > 1:
                result = result + base
            base = base * 10
        return result
        
                