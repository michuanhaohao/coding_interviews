# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:47:04 2017

@author: Luohao
"""

#28 ms 5764K 
class Solution:
    def StrToInt(self, s):
        # write code here
        flag = 1
        if len(s) == 0:
            return 0
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            flag = -1
            s = s[1:]

        temp = [ord(i)-ord('0') for i in s]
        if len(temp) == 0: return 0
        if max(temp) > 9 or min(temp) < 0:
            return 0
        index = 1
        _sum = 0
        while temp != []:
            _sum = _sum + temp.pop()*index
            index = index * 10
        _sum = _sum * flag
        return _sum
        
s = Solution()
result = s.StrToInt('+2147483647') 
result = s.StrToInt('la147483647')        