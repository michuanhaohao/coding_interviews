'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = head
        fast = slow
        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
        start2 = self.reverseList(slow) # 从链表中间开始反转
        while start2 != None:
            if start2.val != head.val:
                return False
            else:
                start2, head = start2.next, head.next
        return True
        
    def reverseList(self, head):
        if head == None:
            return head
        pre = None
        cur = head
        net = cur.next
        while net != None:
            cur.next = pre
            pre, cur, net = cur, net, net.next
        cur.next = pre
        return cur