'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

class Solution(object):
    def __init__(self):
        self.res = []
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.comSum([], candidates, target, 0)
        return self.res
        
    def comSum(self, cur, candidates, target, index):
        if target < 0:
            return
        if target == 0 and len(cur) > 0:
            self.res.append(cur)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.comSum(cur + [candidates[i]], candidates, target - candidates[i], i + 1)