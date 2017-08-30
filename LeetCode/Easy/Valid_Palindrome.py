'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum(): # 判断是否字母数字
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].upper() == s[end].upper():
                start += 1
                end -= 1
            else:
                return False
        return True