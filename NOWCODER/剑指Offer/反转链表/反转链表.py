# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:35:33 2017

@author: Luohao
"""

"""
输入一个链表，反转链表后，输出链表的所有元素。
"""
#38 ms	5720K

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here        
        if pHead == None or pHead.next == None:
            return pHead
        pBefore = None
        while pHead :
            pTemp = pHead.next
            pHead.next = pBefore
            pBefore = pHead
            pHead = pTemp
        return pBefore
            