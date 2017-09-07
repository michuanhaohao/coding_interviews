'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
'''

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        dic = dict(zip(range(1, l + 1), [1] * l))
        rep = 0
        for i in nums:
            if dic.has_key(i):
                if dic[i] == 0:
                    rep = i
                else:
                    dic[i] = 0
        miss = rep + l * (l+1) / 2 - sum(nums)
        return [rep, miss]