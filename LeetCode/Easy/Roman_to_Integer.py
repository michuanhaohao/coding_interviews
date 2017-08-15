'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
'''
1~9: {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

10~90: {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};

100~900: {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};

1000~3000: {"M", "MM", "MMM"}.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d["I"] = 1
        d["V"] = 5
        d['X'] = 10  
        d['L'] = 50  
        d['C'] = 100 
        d['D'] = 500
        d['M'] = 1000
        if len(s)==1:
            return d[s]
        res = d[s[len(s)-1]]
        for i in range(1,len(s))[::-1]: # range(11)表示0到10
            if d[s[i-1]] < d[s[i]]:
                res -= d[s[i-1]]
            else:
                res += d[s[i-1]]
        return res
        