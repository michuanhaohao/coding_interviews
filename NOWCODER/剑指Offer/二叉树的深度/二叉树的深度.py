# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:50:18 2017

@author: Luohao
"""

"""
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#33 ms 5648K 
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = 1
        right = 1
        left = left + self.TreeDepth(pRoot.left)
        right = right + self.TreeDepth(pRoot.right)
        
        return left if left > right else right