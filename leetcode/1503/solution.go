/**
 * https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
 * 1503. Last Moment Before All Ants Fall Out of a Plank
 */

package main

func getLastMoment(n int, left []int, right []int) int {
	longest_l := max(left)
	longest_r := n - min(right)
	if longest_l > longest_r {
		return longest_l
	}
	return longest_r
}

func max(args []int) int {
	if len(args) == 0 {
		return 0
	}
	a := args[0]
	for _, b := range args {
		if a < b {
			a = b
		}
	}
	return a
}

func min(args []int) int {
	if len(args) == 0 {
		return 10001 // maximum value
	}
	a := args[0]
	for _, b := range args {
		if a > b {
			a = b
		}
	}
	return a
}
