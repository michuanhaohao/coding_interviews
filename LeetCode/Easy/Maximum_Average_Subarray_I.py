'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curmax = sum(nums[:k])
        cur = curmax
        l = len(nums)
        for i in range(1, l - k + 1):
            cur = cur - nums[i-1] + nums[i+k-1]
            curmax = max(curmax, cur)
        return float(curmax) / k