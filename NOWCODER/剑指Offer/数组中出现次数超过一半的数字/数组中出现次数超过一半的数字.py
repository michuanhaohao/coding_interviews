# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:39:38 2017

@author: Luohao
"""

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
"""

#36 ms 5764K 
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        sql = {}
        le = len(numbers)
        while numbers != []:
            key = numbers.pop()
            try:
                sql[key] = sql[key] + 1
            except:
                sql[key] = 1
            if sql[key] > le/2:
                return key
        return 0
            
        
s = Solution()
numbers = [1,2,3]
result = s.MoreThanHalfNum_Solution(numbers)