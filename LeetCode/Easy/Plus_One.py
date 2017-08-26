'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits))[::-1]:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        res = []
        if digits[0] == 0:
            res.append(1)
            res.extend(digits) # difference between "extend" and "append"
        return res