/**
 * 1026. Maximum Difference Between Node and Ancestor
 * https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
 */
package lc1026

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func min(vars ...int) (min int) {
	min = vars[0]
	for _, i := range vars {
		if i < min {
			min = i
		}
	}
	return
}

func max(vars ...int) (max int) {
	max = vars[0]
	for _, i := range vars {
		if max < i {
			max = i
		}
	}
	return
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func dfs(node *TreeNode, low, high, answer int) int {
	if node == nil {
		return answer
	}

	// Calculate the highest number among values
	v1 := abs(low - node.Val)
	v2 := abs(high - node.Val)
	answer = max(answer, v1, v2)

	// Determine the lowest and the highest node values
	low = min(low, node.Val)
	high = max(high, node.Val)

	// Calucalte the next nodes
	left := dfs(node.Left, low, high, answer)
	right := dfs(node.Right, low, high, answer)
	return max(left, right)
}

func maxAncestorDiff(root *TreeNode) int {
	return dfs(root, root.Val, root.Val, 0)
}
