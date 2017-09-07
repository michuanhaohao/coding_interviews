'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start = 0 
        end = int(c ** 0.5)
		# a b可以相等
        while start <= int(c ** 0.5) and end >= 0:
            if start ** 2 + end ** 2 == c:
                return True
            elif start ** 2 + end ** 2 > c:
                end -= 1
            else:
                start += 1
        return False