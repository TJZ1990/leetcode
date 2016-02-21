# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        stack = [root]
        depth = 1
        while stack != []:
            l = len(stack)
            for _ in range(l):
                node = stack.pop(0)
                if node.left == None and node.right == None:
                    return depth
                if node.left != None:
                    stack.append(node.left)
                if node.right != None:
                    stack.append(node.right)
            depth += 1
        
                
            
