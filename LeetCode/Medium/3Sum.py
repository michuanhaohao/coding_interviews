'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def __init__(self):
        self.res = []
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) < 3:
            return []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # 去重
            self.findAns(i, nums)
        return self.res
    
    def findAns(self, i, nums):
        target = 0 - nums[i]
        start = i + 1
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                self.res.append([nums[i], nums[start], nums[end]])
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
        