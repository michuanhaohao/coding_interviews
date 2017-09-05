# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:39:05 2017

@author: Luohao
"""

"""
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,
"""

#46 ms 5640K 
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput): return []
        def sort_list(tinput):
            for i in range(len(tinput)):
                for j in range(i+1,len(tinput)):
                    if tinput[i] > tinput[j]:
                        tinput[i],tinput[j] = tinput[j], tinput[i]
            return tinput
        tinput = sort_list(tinput)
        return tinput[:k]

s = Solution()
tinput = [4,5,1,6,2,7,3,8]
r = s.GetLeastNumbers_Solution(tinput,4)