# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:34:52 2017

@author: Luohao
"""

"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root != None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)