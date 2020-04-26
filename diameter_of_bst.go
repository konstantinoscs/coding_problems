//https://leetcode.com/problems/diameter-of-binary-tree/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
    maxd := 0
    longestPath(root, &maxd)
    return maxd
}

func longestPath(root *TreeNode, maxd *int) int {
    var left, right = 0,0
    if root==nil || (root.Left == nil && root.Right == nil) {
        return 0
    }
    
    if root.Left != nil {
        left = 1+ longestPath(root.Left, maxd)
    }
    
    if root.Right != nil {
        right = 1+ longestPath(root.Right, maxd)
    }
    *maxd = Max(*maxd, left+right)
    return Max(left, right)
}

func Max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}