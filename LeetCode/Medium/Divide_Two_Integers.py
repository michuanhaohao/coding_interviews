'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend > 0) ^ (divisor > 0)
        print(negative)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i = i << 1
                temp = temp << 1 # 加速迭代
        if negative:
            res = -res
        if res < -2147483648:
            return -2147483648
        elif res > 2147483647:
            return 2147483647
        return res