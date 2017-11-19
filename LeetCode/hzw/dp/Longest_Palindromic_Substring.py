# [Ebay]
'''
Given a string s, find the longest palindromic substring in s.
input: "babad"  --> output: "bab"
input: "cbbd"   --> output: "bb"
'''

def longestPalindrome(s):
	# Dynamic Programming.
	if not s or len(s) == 0:
		return ""
	n = len(s)
	dp = [[False for j in range(n)] for i in range(n)]
	for i in range(n):
		dp[i][i] = True
	res = s[0]
	# dp[i][j] is True when dp[i+1][j-1] is True and s[i] == s[j]
	# when i > j, when consider it to be an empty string, so it is True
	# diff is the difference between j and i. Since we go through each diagonal.
	for diff in range(1, n):
		for j in range(diff, n):
			i = j-diff
			if s[i] == s[j]:
				if dp[i+1][j-1] or i == j-1:
					dp[i][j] = True
					tmp = s[i:j+1]
					res = res if len(tmp) < len(res) else tmp
	print "input:"
	print s
	print "output:"
	print res
	return res

if __name__ == "__main__":
	ex1 = "abcdef"
	ex2 = "aabbcc"
	ex3 = "abccba"
	ex4 = "abccbd"
	longestPalindrome(ex1)
	longestPalindrome(ex2)
	longestPalindrome(ex3)
	longestPalindrome(ex4)


'''
There is also another way. They have the same TIME COMPLEXITY
for mid in range(n):
	findLongestFromMid(mid, mid) # odd length
	findLongestFromMid(mid, mid+1) #even length if nums[mid+1] == nums[mid]

'''