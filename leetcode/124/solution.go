// 124. Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

package lc124

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Solution struct {
	Root       *TreeNode
	MaxPathSum int
}

func Max(vars ...int) int {
	max := vars[0]
	for _, i := range vars {
		if max < i {
			max = i
		}
	}
	return max
}

func (s *Solution) dfs(node *TreeNode) int {
	if node == nil {
		return 0
	}

	// Get the sum of left and right nodes respectively
	// It the value is less than 0, use 0.
	left := Max(s.dfs(node.Left), 0)
	right := Max(s.dfs(node.Right), 0)
	// Populate curerntPathSum
	curerntPathSum := left + right + node.Val
	// Update answer
	s.MaxPathSum = Max(s.MaxPathSum, curerntPathSum)
	// Compare left and right nodes and return greater one with node.val
	return Max(left, right) + node.Val

}

func NewSolution(root *TreeNode) *Solution {
	s := Solution{Root: root, MaxPathSum: -1001}
	s.dfs(s.Root)
	return &s
}

func maxPathSum(root *TreeNode) int {
	s := NewSolution(root)
	return s.MaxPathSum

}
