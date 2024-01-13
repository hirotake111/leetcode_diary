/*
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/?envType=daily-question&envId=2024-01-05
2385. Amount of Time for Binary Tree to Be Infected
*/
package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Queue struct {
	arr  []*TreeNode
	cur  int
	last int
}

func (q *Queue) push(node *TreeNode) {
	q.arr = append(q.arr, node)
	if q.cur == -1 {
		q.cur = 0
		q.last = 0
	} else {
		q.last++
	}
}

func (q *Queue) pop() *TreeNode {
	if q.isEmpty() {
		return nil
	}
	node := q.arr[q.cur]
	q.cur++
	return node
}

func (q *Queue) isEmpty() bool {
	return q.cur == -1 || q.cur > q.last
}
func (q *Queue) len() int {
	if q.isEmpty() {
		return 0
	}
	return q.last - q.cur + 1
}

func amountOfTime(root *TreeNode, start int) int {
	parents := make(map[*TreeNode]*TreeNode)
	seen := make(map[int]struct{})

	var find_start_node func(node, parent *TreeNode) *TreeNode
	find_start_node = func(node, parent *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		if parent != nil {
			// fmt.Printf("node %d -> parent %d\n", node.Val, parent.Val)
			parents[node] = parent
		}
		if node.Val == start {
			return node
		}
		left := find_start_node(node.Left, node)
		if left != nil {
			return left
		}
		return find_start_node(node.Right, node)
	}

	s := find_start_node(root, nil)
	q := &Queue{arr: make([]*TreeNode, 0), cur: -1, last: -1}
	q.push(s)
	seen[s.Val] = struct{}{}
	minutes := -1
	for !q.isEmpty() {
		minutes++
		count := q.len()
		for i := 0; i < count; i++ {
			node := q.pop()
			if parent, exists := parents[node]; exists {
				if _, exists = seen[parent.Val]; !exists {
					seen[parent.Val] = struct{}{}
					q.push(parent)
				}
			}
			if node.Left != nil {
				if _, exists := seen[node.Left.Val]; !exists {
					seen[node.Left.Val] = struct{}{}
					q.push(node.Left)
				}
			}
			if node.Right != nil {
				if _, exists := seen[node.Right.Val]; !exists {
					seen[node.Right.Val] = struct{}{}
					q.push(node.Right)
				}
			}
		}
	}
	return minutes
}
