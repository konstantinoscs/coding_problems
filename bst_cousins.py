# https://leetcode.com/problems/cousins-in-binary-tree/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    if not root or root.val == x or root.val ==y:
        return False
    xlevel, xparent = self.levelParent(root, None, x, 0)
    ylevel, yparent = self.levelParent(root, None, y, 0)
    if xlevel ==-1 or ylevel ==-1:
        return False
    return xlevel == ylevel and xparent != yparent
    
def levelParent(self, root:TreeNode, parent:TreeNode, x:int, level:int) -> (int, int):
    if not root:
        return -1,-1
        
    if root.val ==x:
        return level, parent.val
        
    rleft = self.levelParent(root.left, root, x, level+1)
    if rleft[0] != -1:
        return rleft
        
    return self.levelParent(root.right, root, x, level+1)