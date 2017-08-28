# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:10:51 2017

@author: Luohao
"""

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
"""

#27 ms	5776K
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        self.stack.append(node)
        if self.min_stack == [] or node <= self.min_stack[-1]:
            self.min_stack.append(node)
        # write code here
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]

#32 ms	5768K
class Solution:
    def __init__(self):
        self.stack = []
    def push(self, node):
        self.stack.append(node)
        # write code here
    def pop(self):
        # write code here
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return min(self.stack)