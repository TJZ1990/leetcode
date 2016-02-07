# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        newHead = start
        for _ in range(m-1):
            newHead = newHead.next
        p = newHead.next
        newEnd = p
        
        for _ in range(n-m+1):
            q = p.next    
            p.next = newHead.next
            newHead.next = p
            p = q
        
        newEnd.next = p
        return start.next
        
            
