# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        big = ListNode(0)
        p = small
        q = big
        m = head
        while m != None:
            if m.val < x:
                p.next = m
                p = m
            else:
                q.next = m
                q = m
            m = m.next
        q.next = None
        p.next = big.next
        return small.next
