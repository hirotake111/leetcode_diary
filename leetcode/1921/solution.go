package main

import "sort"

func eliminateMaximum(dist []int, speed []int) int {
	minutes := make([]int, len(dist))
	for i, d := range dist {
		minutes[i] = d / speed[i]
		if d%speed[i] != 0 {
			minutes[i]++
		}
	}
	sort.Sort(sort.IntSlice(minutes))

	for i, n := range minutes {
		if i >= n {
			return i
		}
	}

	// eliminates all monsters
	return len(dist)
}
