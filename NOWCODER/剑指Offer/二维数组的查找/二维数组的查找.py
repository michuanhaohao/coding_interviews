# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:06:05 2017

@author: Luohao
"""

"""""""""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""""""""
# 302 ms	5760K
class Solution:
    # array 二维列表
    def Find(self, target, array):
        flag = False
        m = len(array)
        try:
            n = len(array[0])
        except:
            return flag
        for i in range(m):
            for j in range(n):
                if target == array[i][j]:
                    flag = True
                    break
            if flag == True:
                break
        return flag


# 300 ms	5764K            
class Solution:
    # array 二维列表
    def Find(self, target, array): 
        def search(target, array_temp):
            begin = 0
            end = len(array_temp)
            index = int(end/2)            
            while(begin < index):
                if target == array_temp[index]:
                    return True
                elif target > array_temp[index]:
                    begin = index
                    index = int((begin+end)/2)
                elif target < array_temp[index]:
                    end = index
                    index = int((begin+end)/2)
            if array_temp[begin] == target:
                return True
            return False
                    
        flag = False
        m = len(array)
        try:
            n = len(array[0])
            if not n:
                return False
        except:
            return flag
        for i in range(m):
            if target >= array[i][0] and target <= array[i][n-1]:
                flag = search(target,array[i])
                print(flag)
                if flag:
                    break
        return flag


#72 ms	9612K
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n=len(array)
        flag='false'
        for i in range(n):
            if target in array[i]:
                flag='true';
                break
        return flag
while True:
    try:
        S=Solution()
        L=list(eval(raw_input()))
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break
#array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
#array=[[]]
target = 1
solution = Solution()
m = solution.Find(target,array)