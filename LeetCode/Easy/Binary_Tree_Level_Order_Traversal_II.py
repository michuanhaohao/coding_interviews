'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = [[root.val]]
        preQueue = [root]
        while len(preQueue) > 0:
            curQueue = []
            temp = []
            for node in preQueue:
                if node.left != None:
                    curQueue.append(node.left)
                    temp.append(node.left.val)
                if node.right != None:
                    curQueue.append(node.right)
                    temp.append(node.right.val)
            if len(temp) > 0:
                res.append(temp)
            preQueue = curQueue
        return res[::-1]
        