'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

'''
DP问题
以抢劫第四个房子结尾的最大收益情况 = max（抢1不抢23，抢2不抢3）+抢4
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 补齐元素，避免对nums长度小于4的情况进行特殊判断
        nums.insert(0,0)
        nums.insert(0,0)
        nums.insert(0,0)
        
        h1 = nums[0]
        h2 = nums[1]
        h3 = nums[2]
        
        for i in nums:
            h3, h2, h1 = i + max(h1,h2), h3, h2
        return max(h3, h2)