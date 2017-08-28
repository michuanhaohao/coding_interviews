'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b) > len(a):
            a,b = b,a
        for i in range(len(a) - len(b)):
            b = "0" + b
        more = 0
        res = ""
        for i in range(len(a))[::-1]:
            if int(a[i]) + int(b[i]) + more > 1:
                res = str(int(a[i]) + int(b[i]) + more - 2) + res
                more = 1
            else:
                res = str(int(a[i]) + int(b[i]) + more) + res
                more = 0
        return "1" + res if more else res