'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        kmp = [0] * (len(s)+1)
        sp = 1
        kp = 0
        while sp < len(s):
            if s[sp] == s[kp]:
                sp += 1
                kp += 1                
                kmp[sp] = kp
            elif kp == 0:
                sp += 1
            else:
                kp = kmp[kp]
        return kmp[-1] != 0 and kmp[-1] % (len(s) - kmp[-1]) == 0