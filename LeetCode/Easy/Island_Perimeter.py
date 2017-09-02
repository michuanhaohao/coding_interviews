'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
'''

'''
对于每一个1的方块，其上下左右有n个1，其贡献的周长为 4 - n
'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res += self.getAround(grid, i, j)
        return res
        
    def getAround(self, grid, i, j):
        res = 4
        if i - 1 >= 0 and grid[i-1][j] == 1:
            res -= 1
        if i + 1 < len(grid) and grid[i+1][j] == 1:
            res -= 1
        if j - 1 >= 0 and grid[i][j-1] == 1:
            res -= 1
        if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
            res -= 1
        return res