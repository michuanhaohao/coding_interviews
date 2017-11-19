# [Ebay]
# find the numbers which is the largest k numbers..
def find_k_percentile(array, k):
	quickSelect(array, 0, len(array)-1, k)
	return array[n-k:]

def quickSelect(array, left, right, k):
	if right == left:
		return
	if right == left+1:
		if array[left] < array[right]:
			return
		else:
			array[left], array[right] = array[right], array[left]
			return
	point = left
	start = left+1
	for i in range(left+1, right+1):
		if array[i] <= array[point]:
			array[start], array[i] = array[i], array[start]
			start += 1
	n = len(array)
	# finally the number in start will be larger than array[point]
	array[point], array[start-1] = array[start-1], array[point]
	# [smaller] point(start-1) [larger]
	#quickSelect(array, left, start-2)
	#quickSelect(array, start, right)
	if start-1 < n-k:
		quickSelect(array, start, right)
	elif start-1 > n-1:
		quickSelect(array, left, start-2)
	else:
		return


