'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''

class Solution(object):
	# My solution
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted(nums)
        start = -1
        end = -2
        for i in range(len(nums)):
            if temp[i] != nums[i]:
                start = i
                break
        for j in range(len(nums))[::-1]:
            if temp[j] != nums[j]:
                end = j
                break
        return end - start + 1

	# Better solution
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = -1
        end = -2
        n = len(nums)
        maxcur = nums[0]
        mincur = nums[-1]
        for i in range(1, n):
            maxcur = max(maxcur, nums[i])
            mincur = min(mincur, nums[n - i - 1])
            if nums[i] != maxcur: # 从0开始到目前为止的最大值，应该排在目前这个位置上
                end = i
            if nums[n - i - 1] != mincur:
                start = n - i - 1
        return end - start + 1
