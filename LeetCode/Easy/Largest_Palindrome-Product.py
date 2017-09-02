'''
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
'''

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        num = int('9' * (n-1) + '8') # When n is Odd, the result is always 99 (n 9s) * 990*1 (n/2 9s with 1)
        if n % 2 == 0:
            num = int('9' * (n/2) + '0' * (n/2))
        while len(str(num)) == n:
            m = int(str(num) + str(num)[::-1])
            for i in range(int(m ** 0.5), int(str('9' * n))+1)[::-1]:
                if m % i == 0:
                    return m % 1337
            num -= 1
        return 0