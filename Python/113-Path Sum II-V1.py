# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.find(root, sum, [], result)
        return result
    
    def find(self, root, sum, curPath, result):
        if root == None:
            return
        sum -= root.val
        if root.left == None and root.right == None and sum == 0:
            result.append(curPath+[root.val])
            return
        curPath.append(root.val)
        self.find(root.left, sum, curPath, result)
        self.find(root.right, sum, curPath, result)
        curPath.pop()
