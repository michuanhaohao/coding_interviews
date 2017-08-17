# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:36:54 2017

@author: Luohao
"""

"""
输入一个链表，从尾到头打印链表每个节点的值。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#39 ms 5636K 
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        head = listNode
        while(head):
            result.insert(0,head.val)
            head = head.next
        return result