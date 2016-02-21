# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        num = 0
        self.head = head
        while head:
            num += 1
            head = head.next
        return self.build(num)
        
    def build(self, num):
        if num == 0:
            return None
        
        root = TreeNode(0)
        root.left = self.build(num/2)
        root.val = self.head.val
        self.head = self.head.next
        root.right = self.build(num-num/2-1)
        return root
        
        
        
        