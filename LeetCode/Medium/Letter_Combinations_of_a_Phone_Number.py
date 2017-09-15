'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        digits.strip('1')
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(s[int(digits[0]) - 2])
        pre = self.letterCombinations(digits[1:])
        res = []
        for c in s[int(digits[0]) - 2]:
            for i in pre:
                res.append(c + i)
        return res