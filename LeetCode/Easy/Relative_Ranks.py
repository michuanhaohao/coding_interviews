'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dic1 = dict(zip(range(len(nums)), nums)) # key, value = index, score
        rank = sorted(dic1.items(), key = lambda e : e[1], reverse = True)
        dic2 = {}
        for i in range(len(rank)):
            if i == 0:
                dic2[rank[i][0]] = "Gold Medal"
                continue
            elif i == 1:
                dic2[rank[i][0]] = "Silver Medal"
                continue
            elif i == 2:
                dic2[rank[i][0]] = "Bronze Medal"
                continue
            dic2[rank[i][0]] = str(i + 1)
        res = []
        for i in range(len(nums)):
            res.append(dic2[i])
        return res
        