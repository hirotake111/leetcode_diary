package main

func countSubTrees(n int, edges [][]int, labels string) []int {
	answer := make([]int, n)

	// Create a tree
	tree := make([][]int, n)
	for _, edge := range edges {
		a := edge[0]
		b := edge[1]
		// Append edge if it's not in the tree
		if !contains(&tree[a], b) {
			tree[a] = append(tree[a], b)
		}
		if !contains(&tree[b], a) {
			tree[b] = append(tree[b], a)
		}
	}

	// recursive function that returns an array of counts with len of 26
	var dfs func(current int, parent int) *[]int
	dfs = func(current int, parent int) *[]int {
		// init counts array with value 0
		counts := make([]int, 26)
		for i := range counts {
			counts[i] = 0
		}

		// iterate child edges in the current tree
		for _, child := range tree[current] {
			// If it's a child, dfs it and combine counts
			if child != parent {
				result := dfs(child, current)
				for i := range counts {
					counts[i] += (*result)[i]
				}
			}
		}

		// Identify index of current edge's word in counts
		idx := rune(labels[current]) - 97
		// Increment value of index in counts
		counts[idx]++
		// Update answer
		answer[current] = counts[idx]
		return &counts
	}

	dfs(0, -1)
	return answer

}

func contains(edges *[]int, target int) bool {
	for _, edge := range *edges {
		if edge == target {
			return true
		}
	}
	return false
}
