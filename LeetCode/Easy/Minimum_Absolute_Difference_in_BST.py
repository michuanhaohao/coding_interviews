'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.mindiff = sys.maxint
        self.pre = None
        
    def getMinimumDifference(self, root):
		# BST 中序遍历
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return self.mindiff
        
        self.getMinimumDifference(root.left)
        if self.pre != None:
            self.mindiff = min(self.mindiff, root.val - self.pre.val)
        self.pre = root
        self.getMinimumDifference(root.right)
        return self.mindiff