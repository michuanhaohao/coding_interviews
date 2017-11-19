# [Ebay]
# find permutations in an array that can sum up to target number.
# example:
# nums: [1,2,3,4], target:3   ---> return [[1,2], [2,1], [3]]
def findPermutation(nums, target):
	nums.sort()
	n = len(nums)
	if target < nums[0] or target > n*nums[n-1]:
		return []

	res = []
	def helper(nums1, target1, tmp, res1):
		if target1 == 0 and len(tmp) != 0:
			res1.append(tmp[:])
		if len(tmp) == len(nums1):
			return

		for num in nums1:
			if num in tmp:
				continue
			tmp.append(num)
			helper(nums1, target1-num, tmp, res1)
			tmp.pop()
		return

	helper(nums, target, [], res)

	print "input: " 
	print nums
	print "target:"
	print target
	print(res)
	return res

if __name__ == "__main__":
	ex1 = [[1,2,3,4],3]
	ex2 = [[1,5,8,-1], 0]
	findPermutation(ex1[0], ex1[1])
	findPermutation(ex2[0], ex2[1])

