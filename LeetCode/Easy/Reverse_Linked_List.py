'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
		# 递归
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        net = head.next
        res = self.reverseList(head.next)
        net.next = head
        head.next = None
        return res
		
    def reverseList(self, head):
		# 非递归，三个node记录
        if head == None or head.next == None:
            return head
        pre = None
        cur = head
        net = cur.next
        while net != None:
            cur.next = pre
            pre = cur
            cur = net
            net = net.next
        cur.next = pre
        return cur