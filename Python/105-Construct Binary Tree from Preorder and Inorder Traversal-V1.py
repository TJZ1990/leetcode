# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        cur = root
        node = None
        i, j = 1, 0
        
        while i < len(preorder):
            if stack != [] and stack[-1].val == inorder[j]:
                node = stack.pop()
                j += 1
            elif node != None:
                cur = TreeNode(preorder[i])
                node.right = cur
                stack.append(cur)
                node = None
                i += 1
            else:
                stack.append(TreeNode(preorder[i]))
                cur.left = stack[-1]
                cur = stack[-1]
                i += 1
                
        return root
        
