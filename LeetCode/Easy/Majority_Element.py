'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == maj:
                count += 1
            else:
                count -= 1
                if count == 0:
                    maj = nums[i+1]
        return maj