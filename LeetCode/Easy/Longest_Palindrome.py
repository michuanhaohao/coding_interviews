'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        res = 0
        oddflag = False
        for i in dic.values():
            if not oddflag:
                if i % 2 == 1:
                    oddflag = True
            res += (i if i % 2 == 0 else i-1)
        return res+1 if oddflag else res