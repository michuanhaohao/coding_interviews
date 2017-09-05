'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return self.isSame(s, t)
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSame(self, r1, r2):
        if r1 == None and r2 == None:
            return True
        if r1 == None or r2 == None:
            return False
        if r1.val != r2.val:
            return False
        return self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)