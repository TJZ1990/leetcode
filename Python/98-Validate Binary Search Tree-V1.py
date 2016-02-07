# The result of in order traverse of BST is a ascending list.



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
        pre = None
        stack = []
        while True:
            while root != None:
                stack.append(root)
                root = root.left
            if stack == []:
                return True
            else:
                root = stack.pop()
                if pre != None and root.val <= pre.val:
                    return False
                pre = root
            root = root.right
            
