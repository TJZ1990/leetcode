# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        stack = [root]
        result = []
        while stack != []:
            l = len(stack)
            temp = []
            for _ in range(l):
                p = stack.pop()
                temp.append(p.val)
                if p.left != None:
                    stack.insert(0, p.left)
                if p.right != None:
                    stack.insert(0, p.right)
            result.insert(0, temp)
        
        return result