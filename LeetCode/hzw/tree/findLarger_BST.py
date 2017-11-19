# [Ebay] 
# Find the smallest number that is larger than the target in a BST
def findLarger(root, target):
	res = sys.maxint
	while root:
		if root.val > target:
			res = min(res, root.val)
			root = root.left
		elif root.val == target:
			root = root.right
		else:
			root = root.right
	return res
