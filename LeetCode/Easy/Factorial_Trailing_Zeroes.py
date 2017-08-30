'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

'''
找5和2因数的个数。
2的个数肯定多于5的个数，所以只用找有多少个5的因数
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n = n/5
            count += n
        return count