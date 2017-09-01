'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dic = Counter(p)
        left = 0
        right = 0
        count = len(p)
        res = []
        while right < len(s):
            '''
            滑动窗口新加入的字符如果在p中存在，且> 0，说明新加入right后，滑动窗口距离目标字符串的差距少1
            如果<= 0，说明滑动字符串中已经有足够的该字符了，新加入right后，不会减少与目标字符串的差距
            仍要记录滑动窗口中比目标字符串多的该字符的个数
            '''
            if dic.has_key(s[right]): 
                if dic[s[right]] > 0: #为正数，表示滑动窗口比目标字符串的该字符还少多少个。反之，多多少个。
                    count -= 1
                dic[s[right]] -= 1    
            right += 1
            
            if count == 0:
                res.append(left)
            '''
            滑动窗口移除left，如果移除的字符在目标字符串中存在，而且>= 0，则移除left后，滑动窗口距离目标字符串的差距多1
            如果< 0，说明该字符在滑动字符串中比目标字符串多，移除left后，不会增加与目标字符串的差距
            仍要记录滑动窗口中比目标字符串少的该字符的个数
            '''
            if right - left == len(p):
                if dic.has_key(s[left]):
                    if dic[s[left]] >= 0:
                        count += 1
                    dic[s[left]] += 1
                left += 1
        return res