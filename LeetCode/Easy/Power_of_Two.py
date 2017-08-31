'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            (n, m) = divmod(n, 2)
            if m != 0:
                return False
        return True # 2**0 = 1