# [Ebay]
# Assume there is no duplicates in the array

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #binary search
        if not nums or len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right) / 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return left if nums[left] == target else -1



# explanation
'''
关键是判断出target会在哪个范围内，是在 [left, mid-1] 还是[mid+1, right]之中？
而
1) when nums[left] <= nums[mid]
                       (rotation)
[left------------mid----max|min------right]
---> if target >= nums[left] and target < mid:
          right = mid-1
     只有在 [left, mid-1] 会出现目标址。
     else:
     	  left = mid+1
'''