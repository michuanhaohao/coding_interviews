# 【Ebay]
#Given a non-empty string s and a dictionary wordDict containing
# a list of non-empty words, determine if s can be segmented into a space-separated\
# sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        wordSet = set(wordDict)
        # dp[i] True means ---> s[:i] can be constructed from wordDict
        for i in range(0, n+1):
            for j in range(0, i):
                if s[j:i] in wordSet:
                    if dp[j]:
                        dp[i] = True
                        break
        return dp[n]
        