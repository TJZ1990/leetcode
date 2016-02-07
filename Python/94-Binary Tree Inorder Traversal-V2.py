# Use a stack.

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
        result = []
        stack = []
        p = root
        while True:
            while p != None:
                stack.append(p)
                p = p.left
            if stack == []:
                break
            p = stack.pop()
            result.append(p.val)
            p = p.right
        return result
