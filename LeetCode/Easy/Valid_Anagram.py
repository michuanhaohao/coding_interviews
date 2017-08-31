'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            if dic.has_key(c):
                dic[c] += 1
            else:
                dic[c] = 1
        for c in t:
            if dic.has_key(c):
                dic[c] -= 1
                if dic[c] == 0:
                    dic.pop(c)
            else:
                return False
        return len(dic) == 0