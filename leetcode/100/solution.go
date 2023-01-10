package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	return search(p, q)
}

func search(a, b *TreeNode) bool {
	// If both don't exist, return true
	if a == nil && b == nil {
		return true
	}
	if a != nil && b != nil {
		// If values are different, return false
		if a.Val != b.Val {
			return false
		}
		// else, return the result of left AND right
		return search(a.Left, b.Left) && search(a.Right, b.Right)
	}
	// One exists but other doesn't -> return false
	return false
}
