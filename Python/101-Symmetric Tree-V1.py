# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        r1 = root.left
        r2 = root.right
        stack1 = []
        stack2 = []
        while True:
            while r1 != None and r2 != None:
                if r1.val != r2.val:
                    return False
                stack1.append(r1)
                stack2.append(r2)
                r1 = r1.left
                r2 = r2.right
            if r1 == None and r2 == None:
                if stack1 == [] and stack2 == []:
                    return True
                else:
                    r1 = stack1.pop()
                    r2 = stack2.pop()
                    r1 = r1.right
                    r2 = r2.left
            else:
                return False
                