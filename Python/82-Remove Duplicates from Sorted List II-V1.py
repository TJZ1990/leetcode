# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        p = newHead
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                q = p.next.next.next
                while q and q.val == p.next.val:
                    q = q.next
                p.next = q
            else:
                p = p.next
        return newHead.next
