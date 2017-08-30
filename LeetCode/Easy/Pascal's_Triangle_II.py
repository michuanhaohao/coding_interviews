'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            temp = [0] + res + [0]
            res = []
            for j in range(len(temp)-1):
                res.append(temp[j] + temp[j+1])
        return res
        