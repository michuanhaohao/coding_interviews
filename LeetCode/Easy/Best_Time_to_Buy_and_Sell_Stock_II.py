'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

'''
贪心法。从前向后遍历数组，只要当天的价格高于前一天的价格，就算入收益。
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                res += prices[i+1] - prices[i]
        return res