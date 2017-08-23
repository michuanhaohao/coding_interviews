# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:40:51 2017

@author: Luohao
"""

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。
队列中的元素为int类型。
"""

#20 ms 5768K 
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        # return xx