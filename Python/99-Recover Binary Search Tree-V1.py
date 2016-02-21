# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        pre = None
        while root != None:
            if root.left != None:
                p = root.left
                while p.right != None and p.right != root:
                    p = p.right
                if p.right == None:
                    p.right = root
                    root = root.left
                else:
                    p.right = None
                    if pre != None and root.val <= pre.val:
                        if first == None:
                            first = pre
                            second = root
                        else:
                            second = root
                    pre = root
                    root = root.right
            else:
                if pre != None and root.val <= pre.val:
                    if first == None:
                        first = pre
                        second = root
                    else:
                        second = root
                pre = root
                root = root.right
        
        first.val, second.val = second.val, first.val