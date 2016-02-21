# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Soluion(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root) != -1
    
    def check(self, root):
        if root == None:
            return 0
        
        l = self.check(root.left)
        if l == -1:
            return -1
        r = self.check(root.right)
        if r == -1:
            return -1
        
        if abs(l-r) > 1:
            return -1
        else:
            return max(l,r) + 1