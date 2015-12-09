#Since k may be bigger than list's length, we should use k%length. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        k = k % length
        tail.next = head
        
        for _ in range(length-k):
            tail = tail.next
            
        newHead = tail.next
        tail.next = None
        head = newHead
        return head
        
            
        
        
        
        
        
        
