'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        if not head:
            return False
        fast = head.next
        while fast != None and slow != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        