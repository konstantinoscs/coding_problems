// https://leetcode.com/problems/binary-tree-maximum-path-sum/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxPathSum(root *TreeNode) int {
    ans := -1 << 31
    ans = Max(ans, maxSum(root, &ans))
    return ans
}

func maxSum(root *TreeNode, ans *int) int {
    if root == nil {
        return -1 << 31
    }
    
    left := maxSum(root.Left, ans)
    right := maxSum(root.Right, ans) 
    //basically: *ans = Max(*ans, left, right, root.Val, left+right+root.Val)
    *ans = Max(*ans, Max(Max(left, right), Max(root.Val, left+right+root.Val)))
    //return max path sum that involves root
    return Max(left+root.Val, Max(root.Val, right+root.Val))
}

func Max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}