/**
 * https://leetcode.com/problems/minimum-time-visiting-all-points/
 * 1266. Minimum Time Visiting All Points
 */
package main

func minTimeToVisitAllPoints(p [][]int) int {
	total := 0
	for i := 0; i < len(p)-1; i++ {
		total += max(abs(p[i][0], p[i+1][0]), abs(p[i][1], p[i+1][1]))
	}
	return total
}

func abs(a int, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
