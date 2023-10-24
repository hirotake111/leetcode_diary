package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestValues(root *TreeNode) []int {
	var answer []int
	queue := []*TreeNode{}

	if root != nil {
		queue = append(queue, root)
	}

	i := -1
	for len(queue) > 0 {
		l := len(queue)
		answer = append(answer, math.MinInt32)
		i += 1
		for j := 0; j < l; j++ {
			node := queue[0]
			queue = queue[1:]
			if answer[i] < node.Val {
				answer[i] = node.Val
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}

	return answer
}

func main() {
	largestValues(&TreeNode{})
}
