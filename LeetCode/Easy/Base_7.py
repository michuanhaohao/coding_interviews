'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        flag = "-" if num < 0 else ""
        res = ""
        num = abs(num)
        while num > 0:
            (m, n) = divmod(num, 7)
            res = str(n) + res
            num = m
        return flag + res