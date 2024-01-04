/**
 * https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
 * 2870. Minimum Number of Operations to Make Array Empty
 */
package main

func minOperations(nums []int) int {
	total := 0
	counter := make(map[int]int)
	for _, n := range nums {
		counter[n]++
	}
	for _, count := range counter {
		ops := 0
		for count > 5 {
			count -= 3
			ops++
		}
		if count == 1 {
			return -1
		}
		if count == 5 || count == 4 {
			total += ops + 2
		} else if count == 3 || count == 2 {
			total += ops + 1
		}
	}
	return total
}
