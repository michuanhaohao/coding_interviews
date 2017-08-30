'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.myReverse(nums, 0, len(nums)-k-1)
        self.myReverse(nums, len(nums)-k, len(nums)-1)
        self.myReverse(nums, 0, len(nums)-1)
    
    def myReverse(self, nums, start, end):
        # nums旋转[start, end]
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1