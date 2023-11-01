// https://leetcode.com/problems/find-mode-in-binary-search-tree/
// 501. Find Mode in Binary Search Tree

package main

func findMode(root *TreeNode) []int {
	// q is a simple version of queue
	// (Using index i allows us to avoid unnecessary pop operation that costs O(n) complexity in Go)
	var q []*TreeNode
	i := 0
	if root != nil {
		q = append(q, root)
	}

	// populate frequency for all numbers using BFS
	freq := make(map[int]int)
	for i < len(q) {
		node := q[i]
		i += 1
		freq[node.Val]++
		if node.Left != nil {
			q = append(q, node.Left)
		}
		if node.Right != nil {
			q = append(q, node.Right)
		}
	}

	// find out the maximum frequency
	maxValue := 0
	for _, count := range freq {
		if count > maxValue {
			maxValue = count
		}
	}

	// collect all numbers that appears maxValue times
	var arr []int
	for n, count := range freq {
		if count == maxValue {
			arr = append(arr, n)
		}
	}

	return arr
}
