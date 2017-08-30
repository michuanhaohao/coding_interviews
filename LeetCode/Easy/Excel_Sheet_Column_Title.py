'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n > 0:
            n -= 1 # key point
            (n, left) = divmod(n, 26)
            res += (chr(left + 65)) # chr(65) = 'A'
        return res[::-1]