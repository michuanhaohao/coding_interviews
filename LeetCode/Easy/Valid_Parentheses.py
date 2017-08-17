'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracketsDic = {"(":")","[":"]","{":"}"}
        for k,v in bracketsDic.items():
            bracketsDic[v] = k
        
        reslist = []
        for i in range(len(s)):
            if len(reslist) == 0:
                reslist.append(s[i])
            elif bracketsDic[s[i]] == reslist[-1]:
                reslist.pop()
            else:
                reslist.append(s[i])
        return True if len(reslist) == 0 else False
        