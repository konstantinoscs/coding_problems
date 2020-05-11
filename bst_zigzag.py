# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = {}
        rev = False
        res = []
        self.traverse(root, 0, levels)
        for row in levels.values():
            if rev:
                row.reverse()
            res.append(row)
            rev = not rev
        return res
        
    def traverse(self, root, lev, levels):
        if not root:
            return
        if lev in levels:
            levels[lev].append(root.val)
        else:
            levels[lev] = [root.val]
        self.traverse(root.left, lev+1, levels)
        self.traverse(root.right, lev+1, levels)