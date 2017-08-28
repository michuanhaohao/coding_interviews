'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        start = 1
        end = x
        while 1:
            mid = (start + end) / 2
            if mid * mid > x:
                end = mid - 1
            else:
                if (mid + 1)*(mid + 1) > x:
                    return mid
                else:
                    start = mid + 1
            