'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        slow = head
        fast = head
        pre = temp
        for i in range(n):
            fast = fast.next
        while fast != None:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next
        return temp.next