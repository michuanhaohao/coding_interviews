'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 冒泡法找到最小的两个负数和最大的三个正数
        for i in range(2):
            for j in range(len(nums) - 1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        minusmin1 = nums[-1]
        minusmin2 = nums[-2]
        
        for i in range(3):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        plusmax1 = nums[-1]
        plusmax2 = nums[-2]
        plusmax3 = nums[-3]
        
        if minusmin1 < 0 and minusmin2 < 0:
            return max(plusmax1 * plusmax2 * plusmax3, plusmax1 * minusmin1 * minusmin2)
        else:
            return plusmax1 * plusmax2 * plusmax3