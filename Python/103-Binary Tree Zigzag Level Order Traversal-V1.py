# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.traverse(result, root, 0)
        return result
    
    def traverse(self, result, root, depth):
        if root == None:
            return
        
        if len(result) == depth:
            result.append([])
            
        if depth % 2 == 0:
            result[depth].append(root.val)
        else:
            result[depth].insert(0, root.val)
        
        self.traverse(result, root.left, depth+1)
        self.traverse(result, root.right, depth+1)