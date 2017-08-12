# -*- coding: utf-8 -*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# 38ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        origin = nums[:] #DeepCopy
        nums.sort()
        start = 0
        end = len(nums) - 1
        while nums[start] + nums[end] != target:
            if nums[start] + nums[end] > target:
                end = end - 1
            else:
                start = start + 1
        return [i for i,v in enumerate(origin) if (v == nums[start] or v == nums[end])]