# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:23:27 2017

@author: Luohao
"""

"""
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
你会不会被他忽悠住？(子向量的长度至少是1)
"""

#43 ms	5768K
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        def MergeArray(array):
            a = array.pop()
            result = []
            while array != []:
                b = array.pop()
                if a*b <= 0:
                    result.append(a)
                    a = b
                else:
                    a += b
            result.append(a)
            if result[0]<=0:
                result = result[1:]
            return result
        def SumArray(array):
            result = [array[0]]
            for i in range(2,len(array),2):
                result.append(result[-1]+array[i-1]+array[i])
            return result
        if array == [] : return 0
        array1 = array[:]
        array = MergeArray(array)
        if len(array) == 0: return max(array1)
        result = []
        while(array != []):
            result.extend(SumArray(array))
            try:
                array = array[2:]
            except:
                break        
        return max(result)
        

s = Solution()
array = [-2,-8,-1,-5,-9]
array =[]
array = [0]
array = [6,-3,-2,7,-15,1,2,2]
a = s.FindGreatestSumOfSubArray(array)
                