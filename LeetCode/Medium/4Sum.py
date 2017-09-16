'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

'''
Solutions one
通过大部分测试用例，少部分超时
'''

class Solution(object):
    def __init__(self):
        self.nums = []
        self.res = []
        self.isSelect = []
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        self.nums = nums
        self.isSelect = [0] * len(nums)
        self.dfs(4, target)
        return self.res
        
    def dfs(self, n, target):
        if n == 1:
            for i in range(len(self.isSelect)):
                if self.isSelect[i] == 0 and self.nums[i] == target:
                    cur = [self.nums[i]]
                    for j in range(len(self.isSelect)):
                        if self.isSelect[j] == 1:
                            cur.append(self.nums[j])
                    cur.sort()
                    if cur not in self.res:
                        self.res.append(cur)
        else:
            for i in range(len(self.isSelect)):
                if self.isSelect[i] == 0:
                    self.isSelect[i] = 1
                    self.dfs(n - 1, target - self.nums[i])
                    self.isSelect[i] = 0
                    
'''
Solution Two
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        def findNSum(nums, target, N, res, results):
            if N == 2:
                start = 0
                end = len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] == target:
                        results.append(res + [nums[start], nums[end]])
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    elif nums[start] + nums[end] > target:
                        end -= 1
                    else:
                        start += 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                        findNSum(nums[i + 1:], target - nums[i], N - 1, res + [nums[i]], results)
        
        results = []
        findNSum(sorted(nums), target, 4, [], results)
        return results