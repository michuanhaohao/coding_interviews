'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
'''

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = copy.deepcopy(M)
        m = len(M)
        n = len(M[0])
        for i in range(m):
            for j in range(n):
                res[i][j] = self.getNeighbors(M, i, j)
        return res
    
    def getNeighbors(self, M, x, y):
        neighbors = [
            M[i][j]
            for i in (x-1, x, x+1)
            for j in (y-1, y, y+1)
            if 0 <= i < len(M) and 0 <= j < len(M[0])
        ]
        return int(sum(neighbors) / len(neighbors))
        
                    