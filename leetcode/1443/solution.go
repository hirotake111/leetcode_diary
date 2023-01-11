package main

func minTime(n int, edges [][]int, hasApple []bool) int {
	// Edge case: no nodes containing apple
	flag := false
	for _, apple := range hasApple {
		flag = flag || apple
	}
	if !flag {
		return 0
	}

	// Create a graph
	graph := make([][]int, n)
	for _, edgeIndexes := range edges {
		edgeA := edgeIndexes[0]
		edgeB := edgeIndexes[1]
		if !contains(graph[edgeA], edgeB) {
			graph[edgeA] = append(graph[edgeA], edgeB)
		}
		if !contains(graph[edgeB], edgeA) {
			graph[edgeB] = append(graph[edgeB], edgeA)
		}
	}

	var dfs func(current, parent int) int
	dfs = func(current, parent int) int {
		subTotal := 0
		for _, child := range graph[current] {
			if child != parent {
				// child index points to a child edge
				subTotal += dfs(child, current)
			}
		}
		if hasApple[current] || 0 < subTotal {
			return subTotal + 2
		}
		return 0
	}

	return dfs(0, -1) - 2
}

func contains(edges []int, target int) bool {
	for edge := range edges {
		if edge == target {
			return true
		}
	}
	return false
}
