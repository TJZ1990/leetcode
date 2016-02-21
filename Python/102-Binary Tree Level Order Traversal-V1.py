# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        stack = [root]
        result = []
        while stack != []:
            cur = []
            nxt = []
            while stack != []:
                p = stack.pop(0)
                cur.append(p.val)
                if p.left != None:
                    nxt.append(p.left)
                if p.right != None:
                    nxt.append(p.right)
            result.append(cur)
            stack = nxt
        return result