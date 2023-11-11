/**
 * https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
 * 1743. Restore the Array From Adjacent Pairs
 */
package main

func restoreArray(adjacentPairs [][]int) []int {
	graph := make(map[int][]int)
	seen := make(map[int]bool)

	// create graph and hash set
	var x, y int
	for _, p := range adjacentPairs {
		x, y = p[0], p[1]
		graph[x] = append(graph[x], y)
		graph[y] = append(graph[y], x)
		add_or_delete(seen, x)
		add_or_delete(seen, y)
	}

	// pick up two values from seen (also clear seen)
	cur := 10_0001
	end := 0
	for k := range seen {
		if cur == 10_0001 {
			cur = k
		} else {
			end = k
		}
		delete(seen, k)
	}

	// create arr
	arr := make([]int, 0, len(graph))
	arr = append(arr, cur)
	seen[cur] = true
	for cur != end {
		v := graph[cur]
		cur = v[0]
		if len(v) == 2 && !seen[v[1]] {
			cur = v[1]
		}
		arr = append(arr, cur)
		seen[cur] = true
	}
	return arr
}

func add_or_delete(s map[int]bool, v int) {
	if _, ok := s[v]; ok {
		// 2nd time -> delete
		delete(s, v)
	} else {
		// 1st time -> add
		s[v] = true
	}
}
