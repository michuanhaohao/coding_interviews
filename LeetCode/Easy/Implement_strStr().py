'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        if n == 0 and haystack == "":
            return 0
        for i in range(len(haystack) - n + 1):
            if needle == haystack[i:i+n]:
                return i
        return -1