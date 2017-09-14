# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:39:13 2017

@author: Luohao
"""

"""
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""

#32 ms 5768K 
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        ugly_list = [0,1,2,3]
        label_index = [2,1,1]
        count = 3
        while count < index:
            temp_list = [2*ugly_list[label_index[0]],3*ugly_list[label_index[1]],5*ugly_list[label_index[2]]]
            temp_ugly = min(temp_list)
            for i in range(3):
                if temp_ugly == temp_list[i]:
                    label_index[i] += 1
            if temp_ugly > ugly_list[-1]:
                ugly_list.append(temp_ugly)
                count +=1
        return ugly_list[index]


s = Solution()
for i in range(20):
    print(s.GetUglyNumber_Solution(i))