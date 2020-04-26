#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    if len(preorder) == 0:
        return None
    head = TreeNode(preorder[0])
    for i in preorder[1:]:
        self.insertToTree(head, i)
        
    return head
    
def insertToTree(self, head, val):
    while True:
        if val>head.val:
            if head.right:
                head = head.right
            else:
                head.right = TreeNode(val)
                break
        else:
            if head.left:
                head = head.left
            else:
                head.left = TreeNode(val)
                break