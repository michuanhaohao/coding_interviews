'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

'''
叶子节点，而且该叶子节点是在其父节点的左边节点才计算
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.sumHelper(root.left, True) + self.sumHelper(root.right, False)
    
    def sumHelper(self, root, isLeft):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val if isLeft else 0
        sleft = self.sumHelper(root.left, True)
        sright = self.sumHelper(root.right, False)
        return sleft + sright