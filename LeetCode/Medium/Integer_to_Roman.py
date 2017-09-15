'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        dic = dict(zip(nums, roman))
        res = ''
        for i in nums:
            while num >= i:
                num -= i
                res += dic[i]
        return res
            