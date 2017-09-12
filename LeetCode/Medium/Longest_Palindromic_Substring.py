'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''

class Solution(object):
    def __init__(self):
        self.res = ''
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        for i in range(len(s) - 1):
            self.extend(s, i, i)
            self.extend(s, i, i+1)
        return self.res
    
    def extend(self, s, i, j):
        start = i
        end = j
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start -= 1
                end += 1
            else:
                break;
        if len(self.res) < end - start - 1:
            self.res = s[start+1:end]
