'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	# 递归
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return max(left, right) + 1
        return min(left, right) + 1
	
	# 广度优先，层序遍历
    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        preQueue = [root]
        flag = True
        while flag:
            curQueue = []
            for node in preQueue:
                if node.left != None:
                    curQueue.append(node.left)
                if node.right != None:
                    curQueue.append(node.right)
                if node.left == None and node.right == None:
                    flag = False
            res += 1
            preQueue = curQueue
        return res