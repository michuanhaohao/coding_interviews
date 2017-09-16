'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def __init__(self):
        self.results = []
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generateLandR('', n, n)
        return self.results
    
    def generateLandR(self, res, left, right):
        if left > 0:
            self.generateLandR(res + '(', left - 1, right)
        if right > left:
            self.generateLandR(res + ')', left, right - 1)
        if right == 0:
            self.results.append(res)
            