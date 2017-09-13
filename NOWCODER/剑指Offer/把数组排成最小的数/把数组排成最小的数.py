# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:18:14 2017

@author: Luohao
"""

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

#32 ms 5764K  python27
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        my_cmp = lambda i,j:int(str(i)+str(j))-int(str(j)+str(i))
        array = sorted(numbers, cmp=my_cmp)
        result = ''
        for num in array:
            result = result + str(num)
        return result 

# python35        
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        from functools import cmp_to_key
        my_cmp = lambda i,j:int(str(i)+str(j))-int(str(j)+str(i))
        my_key = cmp_to_key(my_cmp)
        array = sorted(numbers, key=my_key)
        result = ''
        for num in array:
            result = result + str(num)
        return result      
s = Solution()
numbers = [3,32,321]
result = s.PrintMinNumber(numbers)