# [Ebay] 
# find the mode number in an unsorted array.
# A mode number is the number that appears at least  1/2 times of total numbers.
# [1,2,3,3,3,4] ---> 3
# [1,1,1,1,2,2,2] --->1

def findMode(nums):
	count = 1
	res = nums[0]
	################################################
	## The mode number will get at least n/2 votes.
	## Which will finally make it a winner.
	################################################
	for num in nums:
		if num == res:
			count += 1
		else:
			count -= 1
			if count < 0:
				res = num
				count = 1

	print "input:"
	print nums
	print "output:"
	print res
	print ""
	return res


if __name__ == "__main__":
	ex1 = [1,2,3,3,3,4]
	ex2 = [1,1,3,3,3,1,1]
	ex3 = [0,1,2,3,1,1,4,5,1,1]
	findMode(ex1)
	findMode(ex2)
	findMode(ex3)
