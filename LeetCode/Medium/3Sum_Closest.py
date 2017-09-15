'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object): 
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            cur = target - nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == cur:
                    return target
                elif nums[start] + nums[end] > cur:
                    res = nums[start] + nums[end] + nums[i] if nums[start] + nums[end] - cur < abs(res - target) else res
                    end -= 1
                else:
                    res = nums[start] + nums[end] + nums[i] if cur - nums[start] - nums[end] < abs(res - target) else res
                    start += 1
        return res
        
        