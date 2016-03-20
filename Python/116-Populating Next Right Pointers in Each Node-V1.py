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
        start = root 
        while start != None and start.left != None:
            p = start
            while p.next != None:
                p.left.next = p.right
                p.right.next = p.next.left
                p = p.next
            p.left.next = p.right
            start = start.left
                    
            
