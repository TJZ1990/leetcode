# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        
        newHead = TreeLinkNode(0)
        while root != None:
            newHead.next = None
            curr = newHead
            while root != None:
                if root.left != None:
                    curr.next = root.left
                    curr = curr.next
                if root.right != None:
                    curr.next = root.right
                    curr = curr.next
                root = root.next
            root = newHead.next
            
            
            
            
