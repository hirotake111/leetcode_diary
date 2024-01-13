/*
*
https://leetcode.com/problems/leaf-similar-trees/description/?envType=daily-question&envId=2024-01-05
872. Leaf-Similar Trees
*/
package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	arr1 := dfs(root1)
	arr2 := dfs(root2)
	if len(arr1) != len(arr2) {
		return false
	}
	for i, n := range arr1 {
		if n != arr2[i] {
			return false
		}
	}
	return true
}

func dfs(node *TreeNode) []int {
	if node == nil {
		return []int{}
	}
	if node.Left == nil && node.Right == nil {
		return []int{node.Val}
	}
	arr := make([]int, 0)
	if node.Left != nil {
		arr = append(arr, dfs(node.Left)...)
	}
	if node.Right != nil {
		arr = append(arr, dfs(node.Right)...)
	}
	return arr
}
