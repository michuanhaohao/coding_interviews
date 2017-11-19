# [Ebay]
# Check if a binary tree is subtree of another binary tree.

def checkSubtree(tree1, tree2):
	# check if tree1 is subtree of tree2
	
	# BFS go through tree2
	if not tree1:
		return True
	if not tree2:
		return False
	queue = [tree2]
	while queue:
		current_level = queue[:]
		queue = []
		for node in current_level:
			if node == tree1:
				return True
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

	return False
	