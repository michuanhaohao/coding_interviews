# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:57:23 2017

@author: Luohao
"""

"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
#from IPython import embed

#29 ms	5760K
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ss = list(s)
        ss.reverse()
        result = ''
        while(True):
            try:
                temp = ss.pop()
                if temp == ' ':
                    result = result+"%20"
                else:
                    result = result + temp
            except:
                return result

#28 ms	5756K                        
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = ''
        for i in range(len(s)):
            if s[i] == ' ':
                result = result + "%20"
            else:
                result = result + s[i]
        return result        
        
#28 ms	5760K
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)
        
s = 'We are family'
solu = Solution()
result = solu.replaceSpace(s)