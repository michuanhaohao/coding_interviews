# [Ebay]
# Given two unsorted integer array A and B, find the min difference between A's element and B's element.
# A: [4,1,3,2], B[7,5,10,9] ---> 5-4 = 1; return 1

def findMinDiff(A, B):
	A.sort()
	B.sort()
	if B[0] >= A[-1]:
		return B[0] - A[-1]
	if B[-1] <= A[0]:
		return A[0] - B[-1]
	i = 0
	j = 0
	res = sys.maxint
	while i < len(A) and j < len(B):
		res = min(res, abs(A[i]-B[j]))
		if res == 0:
			return 0
		if A[i] > B[j]:
			j += 1
		else:
			i += 1
	return res