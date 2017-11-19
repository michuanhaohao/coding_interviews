# [Ebay]
'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only 
include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
'''

def findUgly(n):
	if n <= 0:
		return -1
	if n == 1:
		return 1
	t2, t3, t5 = 0, 0, 0
	ugly = [0]*n
	ugly[0] = 1
	for i in range(1,n):
		ugly[i] = min(ugly[t2]*2, ugly[t3]*3, ugly[t5]*5)
		if ugly[i] == ugly[t2]*2:
			t2 += 1
		if ugly[i] == ugly[t3]*3:
			t3 += 1
		if ugly[i] == ugly[t5]*5:
			t5 += 1
	return ugly[n-1]
	