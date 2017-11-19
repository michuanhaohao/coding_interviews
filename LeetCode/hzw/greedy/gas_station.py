# [Ebay]
'''

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # gas[i] - cost[i]
        start = 0
        n = len(gas)
        cur_sum = 0
        total_sum = 0
        for i in range(n):
            total_sum += (gas[i]-cost[i])
            cur_sum += gas[i]
            cur_sum -= cost[i]
            while cur_sum < 0 and start != n-1:
                cur_sum += cost[start]
                cur_sum -= gas[start]
                start += 1
        
        return start if total_sum >= 0 else -1


'''
Find the point from which the following sum will all be larger than 0
'''