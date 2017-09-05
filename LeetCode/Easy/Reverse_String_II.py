'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= len(s):
            return s[::-1]
        start = 0
        res = ''
        while start + k < len(s):
            res += s[start:start + k][::-1]
            start += k
            if start + k >= len(s):
                return res + s[start:]
            else:
                res += s[start:start + k]
                start += k
        return res + s[start:][::-1]