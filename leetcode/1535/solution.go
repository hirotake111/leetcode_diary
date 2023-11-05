/**
 * https://leetcode.com/problems/find-the-winner-of-an-array-game/
 * 1535. Find the Winner of an Array Game
 */

package main

func getWinner(arr []int, k int) int {
	if len(arr) <= k {
		max := arr[0]
		for _, n := range arr {
			if max < n {
				max = n
			}
		}
		return max
	}

	count := 0
	i := 1
	winner := 0
	for count < k {
		if arr[winner] > arr[i] {
			count++
		} else if arr[winner] < arr[i] {
			count = 1
			winner = i
		}
		i = (i + 1) % len(arr)
	}

	return arr[winner]
}
