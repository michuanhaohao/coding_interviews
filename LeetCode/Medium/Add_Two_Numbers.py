'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = ListNode(0)
        pre = res
        while l1 != None or l2 != None or carry != 0:
            temp = ListNode(0)
            if l1 != None:
                temp.val += l1.val
                l1 = l1.next
            if l2 != None:
                temp.val += l2.val
                l2 = l2.next
            temp.val += carry
            if temp.val > 9:
                carry = 1
                temp.val -= 10
            else:
                carry = 0
            pre.next = temp
            pre = temp
        return res.next