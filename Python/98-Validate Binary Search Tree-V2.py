# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, None, None)
    
    def validate(self, root, minVal, maxVal):
        if root == None:
            return True
        if minVal != None and root.val <= minVal:
            return False
        if maxVal != None and root.val >= maxVal:
            return False
        if self.validate(root.left, minVal, root.val) and self.validate(root.right, root.val, maxVal):
            return True
        else:
            return False
