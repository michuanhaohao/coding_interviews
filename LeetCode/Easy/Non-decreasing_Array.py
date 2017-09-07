'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 
4
 to 
1
 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
'''

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count1 = 0
        curmax = nums[0]
        '''
        从前到后，当前值应该是之前出现过的最大值，如果不是，则将其变大
        此情况针对的是对于不符合要求的元素进行增加操作
        因为至多修改一个元素，该元素应该增加或者减小
        '''
        for i in nums:
            if i >= curmax:
                curmax = i
            else:
                count1 += 1
                
        count2 = 0
        curmin = nums[-1]
        '''
        从后到前，当前值应该是之前出现过的最小值，如果不是，则将其变小
        此情况针对的是对于不符合要求的元素进行减小操作
        '''
        for j in nums[::-1]:
            if j <= curmin:
                curmin = j
            else:
                count2 += 1
        return count1 < 2 or count2 < 2
                