'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(1, l)[::-1]:
            if nums[i] > nums[i - 1]:
                # 第i - 1位需要被置换，i - 1后面的都是逆序
                i -= 1
                for j in range(i + 1, l)[::-1]:
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        lo = i + 1
                        hi = l - 1
                        while lo < hi:
                            nums[lo], nums[hi] = nums[hi], nums[lo]
                            lo += 1
                            hi -= 1
                        return
        # 完全逆序
        lo = 0
        hi = l - 1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
