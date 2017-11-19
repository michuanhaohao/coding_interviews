# [Ebay]
# level order traverse Tree.

class TreeNode(object):
	def __init__(self, val);
		self.val = val
		self.left = None
		self.right = None


def traversal(root):
	if not root:
		return []
	res = []
	queue = [root]
	while not queue:
		tmp = queue[:]
		queue = []
		for node in tmp:
			res.append(tmp.val)
			if tmp.left:
				queue.append(tmp.left)
			if tmp.right:
				queue.append(tmp.right)

	return res