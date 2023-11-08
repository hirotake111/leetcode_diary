/**
 * https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
 * 2849. Determine if a Cell is Reachable at a Given Time
 */
package main

func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
	steps := max(abs(sx, fx), abs(sy, fy))
	if t >= 2 {
		return steps <= t
	}
	if t == 0 {
		return steps == 0
	}
	// t == 1
	return steps > 0 && steps <= t
}

func abs(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
