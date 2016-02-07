# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
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
                    result.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right
        return result
