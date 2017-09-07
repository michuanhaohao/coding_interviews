'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.treelist = []
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.inOrder(root)
        start = 0
        end = len(self.treelist) - 1
        while start < end:
            if self.treelist[start] + self.treelist[end] == k:
                return True
            elif self.treelist[start] + self.treelist[end] > k:
                end -= 1
            else:
                start += 1
        return False
        
    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        self.treelist.append(root.val)
        self.inOrder(root.right)