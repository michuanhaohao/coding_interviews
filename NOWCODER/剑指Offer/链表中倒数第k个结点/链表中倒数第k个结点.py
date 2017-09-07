# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:36:37 2017

@author: Luohao
"""

"""
输入一个链表，输出该链表中倒数第k个结点。
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#32 ms 5756K 
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        temp =[]
        while head != None:
            temp.append(head)
            head = head.next
        if k > len(temp) or k<1:
            return 
        return temp[-k]
#32 ms 5756K 
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        pA = head
        for i in range(k):
            try:
                pA = pA.next
            except:
                return None
        while pA != None:
            pA = pA.next
            head = head.next
        return head
                    
        
            