'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
'''

class Solution(object):
    def __init__(self):
        self.res = []
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.comSum([], candidates, target, 0)
        return self.res
        
    def comSum(self, cur, candidates, target, index):
        if index >= len(candidates) or target < 0:
            return
        if target == 0 and len(cur) > 0:
            self.res.append(cur)
            index += 1
        for i in range(index, len(candidates)):
            self.comSum(cur + [candidates[i]], candidates, target - candidates[i], i)
                