'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        res.append([1])
        res.append([1,1])
        if numRows == 1:
            return res[:1]
        if numRows == 2:
            return res[:2]
        for i in range(2,numRows):
            temp = [1]
            pre = res[-1]
            for j in range(len(pre)-1):
                temp.append(pre[j]+pre[j+1])
            temp.append(1)
            res.append(temp)
        return res