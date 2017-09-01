'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num2 = "0" * (len(num1) - len(num2)) + num2
        carry = 0 # 进位
        res = ""
        for i in range(len(num1))[::-1]:
            a = ord(num1[i]) - ord('0')
            b = ord(num2[i]) - ord('0')
            s = a + b + carry
            if s >= 10:
                carry = 1
                s -= 10
            else:
                carry = 0
            res = str(s) + res
        return res if carry == 0 else "1" + res