/*
https://leetcode.com/problems/invert-binary-tree/
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
*/
package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	if root != nil {
		root.Left, root.Right = root.Right, root.Left
		invertTree(root.Left)
		invertTree((root.Right))
	}
	return root
}
