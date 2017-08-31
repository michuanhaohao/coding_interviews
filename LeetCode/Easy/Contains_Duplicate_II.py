'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if dic.has_key(nums[i]):
                if i - dic.get(nums[i]) <= k:
                    return True # 存在一个满足条件即可
                else:
                    dic[nums[i]] = i # 更新
            else:
                dic[nums[i]] = i # 插入
        return False
        