'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = 'qwertyuiop'
        r2 = 'asdfghjkl'
        r3 = 'zxcvbnm'
        res = []
        for s in words:
            res.append(s)
            s = s.lower()
            temp = r3
            if s[0] in r1:
                temp = r1
            elif s[0] in r2:
                temp = r2
            for c in s:
                if c not in temp:
                    res.pop()
                    break
        return res