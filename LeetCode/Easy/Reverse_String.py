'''
Write a function that takes a string as input and returns the string reversed.
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        start = 0
        end = len(slist) - 1
        while start < end:
            slist[start], slist[end] = slist[end], slist[start]
            start += 1
            end -= 1
        return "".join(slist)