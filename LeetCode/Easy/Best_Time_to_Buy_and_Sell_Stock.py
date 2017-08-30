'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''

'''
动态规划法。从前向后遍历数组，记录当前出现过的最低价格，作为买入价格，并计算以当天价格出售的收益，作为可能的最大收益，整个遍历过程中，出现过的最大收益就是所求。
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        curMin = prices[0]
        for i in prices:
            curMin = i if i < curMin else curMin
            res = i - curMin if res < i - curMin else res
        return res