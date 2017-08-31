'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = "aeiou"
        vowels = list(v + v.upper())
        slist = list(s)
        start = 0
        end = len(slist) - 1
        while start < end:
            if not slist[start] in vowels:
                start += 1
                continue
            if not slist[end] in vowels:
                end -= 1
                continue
            slist[start], slist[end] = slist[end], slist[start]
            start += 1
            end -= 1
        return "".join(slist)
            