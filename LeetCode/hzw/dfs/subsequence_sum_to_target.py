# [Ebay]
# Find all subsequnce of the array that adds to the target
def findSub(array, target):
	#Assuming there will be duplicates in the array
	array.sort()
	res = []
	helper(array, 0, [], res)
	return res

def helper(array, pos, tmp, res, target):
	if target == 0:
		res.append(tmp[:])

	for i in range(pos, len(array)):
		tmp.append(array[i])
		helper(array, i+1, tmp, res, target-array[i])
		tmp.pop()
	return	