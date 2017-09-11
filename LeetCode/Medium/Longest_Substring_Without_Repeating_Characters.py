'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        temp = ''
        curlen = 0
        for c in s:
            if c not in temp:
                temp += c
                curlen += 1
            else:
                maxlen = max(maxlen, curlen)
                index = temp.index(c)
                temp = temp[index+1:] + c
                curlen = len(temp)
        return max(maxlen, curlen)