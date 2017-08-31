'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 0
        end = num
        while start <= end:
            mid = (start + end) / 2
            if mid ** 2 == num:
                return True
            if mid ** 2 > num:
                end = mid - 1
            else:
                start = mid + 1
        return False