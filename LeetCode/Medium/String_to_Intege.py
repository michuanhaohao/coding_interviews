'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        str = str.strip()
        if str == None or str == '':
            return 0
        sign = 1
        start = 0
        if str[0] == '+' or str[0] == '-':
            sign = 1 if str[0] == '+' else -1
            start += 1
        res = 0
        for i in range(start, len(str)):
            cur = ord(str[i]) - ord('0')
            if cur > 9 or cur < 0:
                break
            if MAX_INT / 10 < res or MAX_INT / 10 == res and MAX_INT % 10 < cur: # overflow
                return MAX_INT if sign == 1 else MIN_INT
            res = res * 10 + cur
        return sign * res
