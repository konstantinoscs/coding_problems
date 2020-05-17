# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = []
        self.visit(root, inorder)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
        return True
        
    def visit(self, root:TreeNode, inorder):
        if not root:
            return
        self.visit(root.left, inorder)
        inorder.append(root.val)
        self.visit(root.right, inorder)