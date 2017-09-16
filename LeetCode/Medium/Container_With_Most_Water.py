'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''

'''
To compute area, we need to take min(height[i],height[j]) as our height. Thus if height[i]<height[j], then the expression min(height[i],height[j]) will always lead to at maximum height[i] for all other j(i being fixed), so no point checking them. Similarly when height[i]>height[j] then all the other i's can be ignored for that particular j.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        res = 0
        while start < end:
            res = max(res, (end - start) * min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return res