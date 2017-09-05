'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        s = "".join(map(str,flowerbed))
        ss = s.split('1')
        count = 0
        for i in ss:
            if len(i) > 2:
                count += (len(i) - 1) / 2
        if s[:2] == '00': # 开头结尾的0可以额外种一个
            count += 1
        if len(ss) > 1 and s[-2:] == '00': # 保证这个连续的00和开头的不连着
            count += 1
        return count >= n