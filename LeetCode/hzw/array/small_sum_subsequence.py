# [Ebay]
'''
给一个int array和一个int target，返回一个list,包含所有array里面连续的加起来小于target的subsequence。
'''
def findSubseq(array, target):
	# Assuming it only contains positive integers.
	left = 0
	#right = 0
	#cur_sum = 0
	res = []
	n = len(array)
	for i in range(n):
		cur_sum = 0
		for j in range(i, n):
			cur_sum += array[j]
			if cur_sum < target:
				res.append(array[i:j+1])
			else:
				break
	return res

#应该只能强行遍历。
