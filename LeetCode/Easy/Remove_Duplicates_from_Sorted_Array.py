'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
注意超过不重复元素数组的其余部分不用考虑
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        if len(nums) == 0:
            return res
        for i in range(1, len(nums)):
            if nums[i] != nums[res]:
                res += 1
                nums[res] = nums[i]
                
        return res + 1