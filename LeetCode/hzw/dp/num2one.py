# [Ebay]
# Given number N, get the minimun steps reduce N to 1.
# The valid operation is subtract by 1, div by 2, div by 3.


def findSteps(n):
	dp = [sys.maxint for i in range(n+1)]
	dp[1] = 0
	for i in range(2, n+1):
		if i % 3 == 0 and i % 2 == 0:
			dp[i] = 1 + min(dp[i-1], dp[i/2], dp[i/3])
		elif i%3 == 0:
			dp[i] = 1 + min(dp[i-1], dp[i/3])
		elif i % 2 == 0:
			dp[i] = 1 + min(dp[i-1], dp[i/2])
		else:
			dp[i] = 1+dp[i-1]
	return dp[n]
