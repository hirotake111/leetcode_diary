/*
 * https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/?envType=daily-question&envId=2024-01-05
 * 446. Arithmetic Slices II - Subsequence
 */
package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rangeSumBST(root *TreeNode, low int, high int) int {

	return dfs(root, low, high)
}

func dfs(node *TreeNode, low, high int) int {
	var total int
	if node == nil {
		return 0
	}
	if node.Val >= low && node.Val <= high {
		total += node.Val
	}
	if node.Left != nil && node.Val > low {
		total += dfs(node.Left, low, high)
	}
	if node.Right != nil && node.Val < high {
		total += dfs(node.Right, low, high)
	}
	return total
}
