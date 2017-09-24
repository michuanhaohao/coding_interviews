'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        def search(start, end):
            if nums[start] == target == nums[end]:
                return [start, end]
            if nums[start] <= target <= nums[end]:
                mid = (start + end) / 2
                left = search(start, mid)
                right = search(mid + 1, end)
                if -1 in left:
                    return right
                elif -1 in right:
                    return left
                else:
                    return [left[0], right[1]]
            return [-1, -1]
        res = search(0, len(nums) - 1)
        return res