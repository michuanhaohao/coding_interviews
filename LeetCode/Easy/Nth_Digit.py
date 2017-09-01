'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 9
        while n > base*len(str(base)):
            n -= base*len(str(base))
            base *= 10 # 一位数有9个，两位数有90个，三位数有900个，以此类推
        basestart = base / 9
        baselen = len(str(base))
        (d, m) = divmod(n, baselen) # 从基准数1,10,100开始又过了几个数
        basestart += d
        if m == 0:
            return int(str(basestart-1)[-1])
        return int(str(basestart)[m-1])
        