# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        node = None
        cur = root
        i, j = len(inorder)-1, len(postorder)-2
        
        while j >= 0:
            if stack != [] and stack[-1].val == inorder[i]:
                node = stack.pop()
                i -= 1
            elif node != None:
                cur = TreeNode(postorder[j])
                node.left = cur
                stack.append(cur)
                node = None
                j -= 1
            else:
                cur.right = TreeNode(postorder[j])
                cur = cur.right
                stack.append(cur)
                j -= 1
        
        return root
                
                
                