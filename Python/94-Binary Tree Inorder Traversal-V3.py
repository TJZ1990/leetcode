# Morris Traversal
# It's similar to threaded binary tree.
# O(1) space, O(n) time. Every path is walked at most three times.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        result = []
        while cur != None:
            if cur.left == None:
                result.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right != None and pre.right != cur:
                    pre = pre.right
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    result.append(cur.val)
                    cur = cur.right
        
        return result 
