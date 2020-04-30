//no dedicated problem page so I'm putting the description here
/*"Given a binary tree where each path going from the root to any leaf form a valid sequence, 
check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all 
values of the nodes along a path results in a sequence in the given binary tree."*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidSequence(root *TreeNode, arr []int) bool {
    return validSequence(root, arr, 0)
}

func validSequence(root *TreeNode, arr []int, idx int) bool {
    if root == nil || root.Val != arr[idx] {
        return false
    }
    if idx == len(arr) -1 {
        if root.Left == nil && root.Right == nil {
            return true
        }
        return false
    }
    
    return validSequence(root.Left, arr, idx+1) || validSequence(root.Right, arr, idx+1)
    
}