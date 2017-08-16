'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==0):
            return ""
        shortest = len(strs[0])
        for s in strs:
            shortest = len(s) if shortest > len(s) else shortest
        res = ""
        flag = True
        for i in range(shortest):
            temp = strs[0][i]
            res = res + temp
            for s in strs:
                if s[i] == temp:
                    continue
                else:
                    flag = False
                    break
            if(not flag):
                break
        return res if flag else res[0:len(res)-1]