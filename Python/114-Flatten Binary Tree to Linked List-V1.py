# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        p = TreeNode(0)
        stack = []
        while True:
            while root != None:
                root.left, root.right = root.right, root.left
                p.right = root
                p = p.right
                stack.append(root)
                root = root.right
            if stack == []:
                return
            q = stack.pop()
            root = q.left
            q.left = None
